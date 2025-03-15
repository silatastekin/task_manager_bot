#SILA TAŞTEKİN
import discord
from discord.ext import commands
import sqlite3
import aiohttp
import asyncio
import ssl

# SSL doğrulamasını devre dışı bırak
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Özel HTTP istemcisi oluştur
async def create_http_client():
    connector = aiohttp.TCPConnector(ssl=ssl_context)
    return aiohttp.ClientSession(connector=connector)

# Bot ayarları
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot başlatıldığında özel HTTP istemcisini oluştur
@bot.event
async def on_ready():
    bot.http_client = await create_http_client()
    print(f'Bot {bot.user} olarak giriş yaptı!')

# Veritabanı bağlantısını güvenli bir şekilde açan fonksiyon
def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

@bot.command()
async def add_task(ctx, *, description):
    """Yeni bir görev ekler."""
    with get_db_connection() as conn:
        conn.execute('INSERT INTO tasks (description, completed) VALUES (?, ?)', (description, 0))
        conn.commit()
    await ctx.send(f'Görev eklendi: {description}')

@bot.command()
async def delete_task(ctx, task_id: int):
    """Belirtilen ID'ye sahip görevi siler."""
    with get_db_connection() as conn:
        conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
    await ctx.send(f'Görev silindi: {task_id}')

@bot.command()
async def show_tasks(ctx):
    """Tüm görevleri listeler."""
    with get_db_connection() as conn:
        tasks = conn.execute('SELECT * FROM tasks').fetchall()
    
    if tasks:
        task_list = "\n".join([f"{task['id']}: {task['description']} {'(Tamamlandı)' if task['completed'] else ''}" for task in tasks])
        await ctx.send(f"Görevler:\n{task_list}")
    else:
        await ctx.send("Hiç görev bulunamadı.")

@bot.command()
async def complete_task(ctx, task_id: int):
    """Belirtilen görevi tamamlanmış olarak işaretler."""
    with get_db_connection() as conn:
        conn.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
        conn.commit()
    await ctx.send(f'Görev tamamlandı: {task_id}')

# Botu çalıştır (TOKEN'ı güvenli bir şekilde sakladığınızdan emin olun)
bot.run('sizinbottokeniniz')
