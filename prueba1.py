import yt_dlp
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8943757533:AAHNS7lMxyv1Bt6iRFeWxkbZPoOCxFlB4S4"

async def start(update: Update, context):
    await update.message.reply_text("Mándame un link de TikTok y te lo bajo sin marca we 🔥")

async def descargar(update: Update, context):
    url = update.message.text
    if "tiktok.com" not in url:
        await update.message.reply_text("Ese no es link de TikTok")
        return

    await update.message.reply_text("Bajándolo...")

    ydl_opts = {'format': 'mp4', 'outtmpl': 'video.mp4', 'quiet': True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        await update.message.reply_video(video=open('video.mp4', 'rb'))
    except Exception as e:
        await update.message.reply_text(f"Valió: {e}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, descargar))
app.run_polling()
