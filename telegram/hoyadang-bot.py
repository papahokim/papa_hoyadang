#!/usr/bin/env python3
"""
hoyadang-bot.py — 好爺堂 1:1 회의실 봇
@hoyadang_bot — Boss ↔ 好爺堂 직접 소통 채널

실행: python3 hoyadang-bot.py
환경: TG_TOKEN 환경변수 또는 config.json
"""

import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime, timezone

try:
    from telegram import Update, BotCommand
    from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
except ImportError:
    print("[ERROR] python-telegram-bot 미설치. pip install python-telegram-bot==20.7")
    sys.exit(1)

SCRIPT_DIR = Path(__file__).parent
REPO_DIR = SCRIPT_DIR.parent
CONFIG_FILE = SCRIPT_DIR / "config.json"
LOG_FILE = SCRIPT_DIR / "hoyadang-bot.log"

config = {}
if CONFIG_FILE.exists():
    with open(CONFIG_FILE) as f:
        config = json.load(f)

BOT_TOKEN = os.getenv("TG_TOKEN") or config.get("bot_token", "")
BOT_NAME = config.get("bot_name", "hoyadang_bot")
DISPLAY_NAME = config.get("display_name", "好爺堂 — 1:1 회의실")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_FILE, encoding="utf-8"), logging.StreamHandler()],
)
logger = logging.getLogger("hoyadang-bot")

LIVE_PAGES = {
    "호야당": "https://papahokim.github.io/papa_hoyadang/",
    "파파플라이": "https://papahokim.github.io/papa_fly/",
    "레포": "https://github.com/papahokim/papa_hoyadang",
}

DELIVERY_LINKS = {
    "쿠팡이츠": "https://web.coupangeats.com/share?storeId=550712",
    "배달의민족": "https://s.baemin.com/d2000gCVdxUak",
    "요기요": "https://ws.yogiyo.co.kr/jnsce1",
}

MEETING_GREETING = """🍞 *好爺堂 — 1:1 회의실*에 오신 것을 환영합니다.

20년 장인의 손맛, K-Street Food IP

📋 *명령어*
/start — 회의 시작
/status — 시스템 상태
/menu — 메뉴 / 배달 링크
/log — 작업 로그
/deploy — 배포 확인
/page — 라이브 페이지
/health — 건강 검진
/help — 도움말

무엇을 도와드릴까요?"""

HELP_TEXT = """🍞 *好爺堂 회의실 — 도움말*

Boss ↔ 好爺堂 간 1:1 회의록 및 모니터링 채널입니다.

*명령어*
• `/start` — 회의실 입장
• `/status` — 시스템 상태
• `/menu` — 메뉴·배달 링크
• `/log` — 작업 기록
• `/deploy` — 배포 상태
• `/page` — 라이브 페이지
• `/health` — 건강 검진
• `/help` — 도움말

*배달앱* — 쿠팡이츠·배민·요기요 자동 헬스체크

📡 https://papahokim.github.io/papa_hoyadang/"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    logger.info(f"회의 시작: {user.full_name}")
    await update.message.reply_text(
        f"안녕하세요, {user.full_name}님!\n\n{MEETING_GREETING}",
        parse_mode="Markdown",
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT, parse_mode="Markdown")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    msg = f"""📊 *好爺堂 시스템 상태*
🕐 {now}

📦 *레포*
• [github.com/papahokim/papa_hoyadang](https://github.com/papahokim/papa_hoyadang)

🌐 *라이브*
• {LIVE_PAGES['호야당']}

🛵 *배달앱*
• 쿠팡이츠: [주문]({DELIVERY_LINKS['쿠팡이츠']})
• 배민: [주문]({DELIVERY_LINKS['배달의민족']})
• 요기요: [주문]({DELIVERY_LINKS['요기요']})

📋 *상태*: ✅ 운영 중"""
    await update.message.reply_text(msg, parse_mode="Markdown", disable_web_page_preview=True)


async def menu_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lines = ["🍞 *好爺堂 메뉴 / 배달*\n"]
    for name, url in DELIVERY_LINKS.items():
        lines.append(f"• [{name} 주문하기]({url})")
    lines.append(f"\n📋 [전체 메뉴 보기]({LIVE_PAGES['호야당']}/menu/)")
    await update.message.reply_text("\n".join(lines), parse_mode="Markdown")


async def deploy_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pages_check = []
    for name, url in LIVE_PAGES.items():
        try:
            import urllib.request
            req = urllib.request.Request(url)
            res = urllib.request.urlopen(req, timeout=10)
            pages_check.append(f"✅ {name}: HTTP {res.status}")
        except Exception as e:
            pages_check.append(f"❌ {name}: {e}")

    msg = "🚀 *배포 상태*\n\n" + "\n".join(pages_check)
    await update.message.reply_text(msg, parse_mode="Markdown")


async def page_urls(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "🌐 *好爺堂 라이브 페이지*\n\n"
    for name, url in LIVE_PAGES.items():
        msg += f"• *{name}*: {url}\n"
    await update.message.reply_text(msg, parse_mode="Markdown")


async def work_log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    devlog_dir = REPO_DIR / "devlog"
    logs = []
    if devlog_dir.exists():
        for f in sorted(devlog_dir.glob("*.md"), reverse=True)[:5]:
            logs.append(f"📝 {f.name}")
    if not logs:
        logs.append("📝 로그 없음")
    await update.message.reply_text("📋 *최근 작업 로그*\n\n" + "\n".join(logs), parse_mode="Markdown")


async def health_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    health_script = REPO_DIR / "phone-health.sh"
    msg_parts = ["🏥 *好爺堂 건강 검진*\n"]
    if health_script.exists():
        try:
            import subprocess
            result = subprocess.run(
                ["bash", str(health_script)],
                capture_output=True, text=True, timeout=30, cwd=str(REPO_DIR)
            )
            if result.returncode == 0:
                msg_parts.append("✅ 시스템 정상")
                for line in result.stdout.strip().split("\n")[-8:]:
                    msg_parts.append(line)
            else:
                msg_parts.append(f"⚠️ 검진 실패: {result.stderr[:200]}")
        except Exception as e:
            msg_parts.append(f"❌ 검진 오류: {e}")
    else:
        msg_parts.append("⚠️ phone-health.sh 없음")
    await update.message.reply_text("\n".join(msg_parts), parse_mode="Markdown")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text or ""

    meeting_log = SCRIPT_DIR / "meetings"
    meeting_log.mkdir(exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = meeting_log / f"meeting-{today}.md"
    timestamp = datetime.now().strftime("%H:%M")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n**{timestamp} — {user.full_name}:**\n{text}\n")

    logger.info(f"DM from {user.full_name}: {text[:100]}")

    reply = f"📝 *회의록 저장 완료* ({timestamp})\n\n"
    reply += "도움이 필요하시면 /help 를 입력하세요."

    await update.message.reply_text(reply, parse_mode="Markdown")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Error: {context.error}")


def main():
    if not BOT_TOKEN:
        print("❌ TG_TOKEN 환경변수 또는 config.json에 bot_token이 필요합니다.")
        sys.exit(1)

    logger.info(f"🍞 {DISPLAY_NAME} 시작 중...")
    logger.info(f"   Bot: @{BOT_NAME}")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("menu", menu_cmd))
    app.add_handler(CommandHandler("deploy", deploy_status))
    app.add_handler(CommandHandler("page", page_urls))
    app.add_handler(CommandHandler("log", work_log))
    app.add_handler(CommandHandler("health", health_check))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)

    async def set_commands(app):
        commands = [
            BotCommand("start", "회의 시작"),
            BotCommand("status", "시스템 상태"),
            BotCommand("menu", "메뉴 / 배달 링크"),
            BotCommand("log", "작업 로그"),
            BotCommand("deploy", "배포 확인"),
            BotCommand("page", "라이브 페이지"),
            BotCommand("health", "건강 검진"),
            BotCommand("help", "도움말"),
        ]
        await app.bot.set_my_commands(commands)

    app.post_init = set_commands

    logger.info("✅ 봇 시작! Ctrl+C로 종료")
    app.run_polling()


if __name__ == "__main__":
    main()
