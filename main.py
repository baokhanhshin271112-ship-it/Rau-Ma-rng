
import os
import random
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree  # Slash command manager

# Danh sách 37 cấp độ rau má
rau_ma_levels = [
    "❌ Cấp 0 – Chúc bạn may mắn lần sau",
    "🥬 Cấp 1 – Rau má thường",
    "🍃 Cấp 2 – Rau má non",
    "☘️ Cấp 3 – Rau má tươi xanh",
    "🌿 Cấp 4 – Rau má hữu cơ",
    "🌱 Cấp 5 – Rau má sạch VietGAP",
    "💧 Cấp 6 – Rau má mọng nước",
    "🌸 Cấp 7 – Rau má hoa hồng",
    "🔥 Cấp 8 – Rau má cay nồng",
    "🌈 Cấp 9 – Rau má cầu vồng",
    "🌙 Cấp 10 – Rau má đêm trăng",
    "☀️ Cấp 11 – Rau má bình minh",
    "🌧️ Cấp 12 – Rau má sau mưa",
    "🌾 Cấp 13 – Rau má đồng xanh",
    "🍀 Cấp 14 – Rau má may mắn",
    "🎋 Cấp 15 – Rau má thần tre",
    "💎 Cấp 16 – Rau má pha lê",
    "⚡ Cấp 17 – Rau má sấm sét",
    "🌪️ Cấp 18 – Rau má lốc xoáy",
    "🌋 Cấp 19 – Rau má núi lửa",
    "❄️ Cấp 20 – Rau má băng giá",
    "🌊 Cấp 21 – Rau má đại dương",
    "🌌 Cấp 22 – Rau má vũ trụ",
    "🪐 Cấp 23 – Rau má sao Thổ",
    "🌠 Cấp 24 – Rau má sao băng",
    "☄️ Cấp 25 – Rau má thiên thạch",
    "👑 Cấp 26 – Rau má hoàng gia",
    "🐉 Cấp 27 – Rau má long thần",
    "🦄 Cấp 28 – Rau má kỳ lân",
    "👻 Cấp 29 – Rau má ma thuật",
    "⚜️ Cấp 30 – Rau má cổ đại",
    "💫 Cấp 31 – Rau má ánh sáng",
    "🌟 Cấp 32 – Rau má tinh tú",
    "🔥 Cấp 33 – Rau má huyền thoại",
    "🧠 Cấp 34 – Rau má trí tuệ",
    "🏆 Cấp 35 – Rau má siêu cấp thượng thừa",
    "👼 Cấp 36 – Rau má tối thượng"
]

# Lưu dữ liệu người chơi (tạm)
user_data = {}

@bot.event
async def on_ready():
    print(f"✅ Rau Má RNG online dưới tài khoản: {bot.user}")
    await tree.sync()
    print("🌿 Slash commands đã sync với Discord!")

# /roll
@tree.command(name="roll", description="Quay rau má ngẫu nhiên và nhận exp!")
async def roll(interaction: discord.Interaction):
    user_id = interaction.user.id
    level = random.randint(0, 36)
    exp_gain = level + 1  # Cấp càng cao exp càng nhiều

    if user_id not in user_data:
        user_data[user_id] = {"rolls": 0, "exp": 0}
    user_data[user_id]["rolls"] += 1
    user_data[user_id]["exp"] += exp_gain

    await interaction.response.send_message(
        f"🎲 {interaction.user.mention} roll được **{rau_ma_levels[level]}** (+{exp_gain} exp)\n"
        f"📈 Tổng: {user_data[user_id]['rolls']} roll, {user_data[user_id]['exp']} exp"
    )

# /top_rolls
@tree.command(name="top_rolls", description="Xem bảng xếp hạng số lần roll nhiều nhất")
async def top_rolls(interaction: discord.Interaction):
    if not user_data:
        await interaction.response.send_message("📉 Chưa ai roll cả bro!")
        return

    sorted_data = sorted(user_data.items(), key=lambda x: x[1]["rolls"], reverse=True)
    leaderboard = "\n".join([
        f"#{i+1} <@{user_id}> — {data['rolls']} lần roll"
        for i, (user_id, data) in enumerate(sorted_data[:10])
    ])
    await interaction.response.send_message(f"🏆 **Top 10 Rollers:**\n{leaderboard}")

# /top_exp
@tree.command(name="top_exp", description="Xem bảng xếp hạng EXP cao nhất")
async def top_exp(interaction: discord.Interaction):
    if not user_data:
        await interaction.response.send_message("📉 Chưa ai có exp cả bro!")
        return

    sorted_data = sorted(user_data.items(), key=lambda x: x[1]["exp"], reverse=True)
    leaderboard = "\n".join([
        f"#{i+1} <@{user_id}> — {data['exp']} exp"
        for i, (user_id, data) in enumerate(sorted_data[:10])
    ])
    await interaction.response.send_message(f"🌟 **Top 10 EXP Kings:**\n{leaderboard}")

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Rau má RNG still rolling 🌿"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# Gọi hàm này trước khi bot.run()
keep_alive()
bot.run(TOKEN)
