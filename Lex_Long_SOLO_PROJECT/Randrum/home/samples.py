import random

kick_list = [
    {"name": "Kick_Ninja", "link": "https://dl.dropboxusercontent.com/s/wwr8ww4mzwo3in9/Bassdrum-01.wav?dl=1"},
    {"name": "Kick_808", "link": "https://dl.dropboxusercontent.com/s/ny3pdtqso1zou20/Bassdrum-02.wav?dl=1"},
    {"name": "Kick_Hard", "link": " https://dl.dropboxusercontent.com/s/r5283t60zqvplis/Kick%20%2836%29.wav?dl=1"},
    {"name": "Kick_DMX", "link": "https://dl.dropboxusercontent.com/s/y1xt89hzplnyd54/Bassdrum-03.wav?dl=1"},
    {"name": "Kick_Real", "link": "https://dl.dropboxusercontent.com/s/3k88p19e71136rv/Real_Kick.wav?dl=1"},
    {"name": "Kick_SP12", "link": "https://dl.dropboxusercontent.com/s/m6j8j7bsaqt3tge/Bassdrum-01.wav?dl=1"},
    {"name": "Kick_Smoothie", "link": "https://dl.dropboxusecontent.com/s/5h7urpvtlyjw0nu/Bassdrum-37.wav?dl=1"},
    {"name": "Kick_Synth", "link": "https://dl.dropboxusercontent.com/s/hunnef4294xhml8/Bassdrum.wav?dl=1"},
    {"name": "Kick_CodingDojo", "link": "https://dl.dropboxusercontent.com/s/ukcikjq7j2j164l/CodingDojo_Kick.wav?dl=1"},
    {"name": "Kick_Nice:", "link": "https://dl.dropboxusercontent.com/s/wc6h1uawsfmbz8u/Nice.wav?dl=1"}
]

snare_list = [
    {"name":"Snare_Nice", "link":"https://dl.dropboxusercontent.com/s/fkmb1x7bue4o2m9/Snaredrum.wav?dl=1"},
    {"name":"Snare_Lucky", "link":"https://dl.dropboxusercontent.com/s/9dza40pp7durqrv/Snaredrum-07.wav?dl=1"},
    {"name":"Snare_Clean", "link":"https://dl.dropboxusercontent.com/s/qe7r9jmxxdf96zj/Snaredrum-02.wav?dl=1"},
    {"name":"Snare_Fake", "link":"https://dl.dropboxusercontent.com/s/nwlem2u55u3ey8j/Snaredrum-17.wav?dl=1"},
    {"name":"Snare_Medium", "link":"https://dl.dropboxusercontent.com/s/kdng7xk4knv4yqe/Snaredrum-02.wav?dl=1"},
    {"name":"Snare_Real", "link":"https://dl.dropboxusercontent.com/s/bww8kj5lagat09a/RealSnare1.wav?dl=1"},
    {"name":"Snare_Lars", "link":"https://dl.dropboxusercontent.com/s/pobrli9hpjlt95r/Snare%20%285%29.wav?dl=1"},
    {"name":"Snare_Dusty", "link":"https://dl.dropboxusercontent.com/s/0kbsn7i052rwksm/Snare%20%2816%29.wav?dl=1"},
    {"name":"Snare_909", "link":"https://dl.dropboxusercontent.com/s/q60uijpl1mmgmtv/ST3T0S7.WAV?dl=1"},
    {"name":"Snare_Deep", "link":"https://dl.dropboxusercontent.com/s/ljka9mi3dzvd9h5/Deep.wav?dl=1"},
]

HHcl_list = [
    {"name":"HHcl_808","link":"https://dl.dropboxusercontent.com/s/35mdtltu4laaphg/Hat%20Closed.wav?dl=1"},
    {"name":"HHcl_909","link":"https://dl.dropboxusercontent.com/s/qa9j8fi283ty2xp/HHCD4.WAV?dl=1"},
    {"name":"HHcl_Fire","link":"https://dl.dropboxusercontent.com/s/f4yxwjk985uodtv/Hat%20Closed-01.wav?dl=1"},
    {"name":"HHcl_Collision","link":"https://dl.dropboxusercontent.com/s/vpwn6jruswc8lwe/Hat%20Closed.wav?dl=1"},
    {"name":"HHcl_Vapor","link":"https://dl.dropboxusercontent.com/s/vlhpuv8c1qpgfg9/CYMBAL_024.wav?dl=1"},
    {"name":"HHcl_Old","link":"https://dl.dropboxusercontent.com/s/mvk0xcr5o31hmk6/Closed%20Hat.wav?dl=1"},
    {"name":"HHcl_Bird","link":"https://dl.dropboxusercontent.com/s/ygsov3qw9vjctqh/Hat%20Closed.wav?dl=1"},
    {"name":"HHcl_Real","link":"https://dl.dropboxusercontent.com/s/3qvk3chl6felhjc/RealHHcl.wav?dl=1"},
    {"name":"HHcl_Python","link":"https://dl.dropboxusercontent.com/s/fodzatigqr55euo/Hat%20Closed.wav?dl=1"},
    {"name":"HHcl_Extra","link":"https://dl.dropboxusercontent.com/s/2lmnuzm2jvll0ug/extra.wav?dl=1"},
]

HHop_list = [
    {"name":"HHop_ninja","link":"https://dl.dropboxusercontent.com/s/qvt3nmlcbe97p00/Ninja_HHop.WAV?dl=1"},
    {"name":"HHop_Real","link":"https://dl.dropboxusercontent.com/s/rkekcb4v1dbezb6/Real_HHop.WAV?dl=1"},
    {"name":"HHop_House","link":"https://dl.dropboxuserconent.com/s/03qeruegxim454d/House_HHop.WAV?dl=1"},
    {"name":"HHop_Long","link":"https://dl.dropboxusercontent.com/s/jby1aimcowr4jtt/Hat%20Open.wav?dl=1"},
    {"name":"HHop_Shine","link":"https://dl.dropboxusercontent.com/s/t6su80jbu3nai80/Hat%20Open.wav?dl=1"},
    {"name":"HHop_Electro","link":"https://dl.dropboxusercontent.com/s/r9bod2je6bhs10s/Hat%20Open.wav?dl=1"},
    {"name":"HHop_","link":"https://dl.dropboxusercontent.com/s/ouj9nqv6kphf445/Hat%20Open-02.wav?dl=1"},
    {"name":"HHop_","link":"https://dl.dropboxusercontent.com/s/n5m9cry63vo80v7/Hat%20Open.wav?dl=1"},
    {"name":"HHop_","link":"https://dl.dropboxusercontent.com/s/21hyk3jiqf35avl/Hat%20Open.wav?dl=1"},
    {"name":"HHop_","link":"https://dl.dropboxusercontent.com/s/67mbnk5kr5bk21y/Hat%20Open.wav?dl=1"},
]

TomH_list = [
    {"name":"TomH_Boop","link":"https://dl.dropboxusercontent.com/s/cm8obyt7m80oeza/Achitom1.wav?dl=1"},
    {"name":"TomH_Linn","link":"https://dl.dropboxusercontent.com/s/c175ne5vfa8l7cu/Tom-01.wav?dl=1"},
    {"name":"TomH_DR550","link":"https://dl.dropboxusercontent.com/s/jv0bj1gm665kwyb/Tom%20H-01.wav?dl=1"},
    {"name":"TomH_Sensei","link":" https://dl.dropboxusercontent.com/s/n0nehc5n39cn38v/Sensei.wav?dl=1"},
    {"name":"TomH_Ace","link":"https://dl.dropboxusercontent.com/s/km4zvtix9ha8z24/Tom-09.wav?dl=1"},
    {"name":"TomH_808","link":"https://dl.dropboxusercontent.com/s/janp15502w2cgku/Tom%20H.wav?dl=1"},
    {"name":"TomH_909","link":"https://dl.dropboxusercontent.com/s/51l4zjra340kwae/Tom%20H.wav?dl=1"},
    {"name":"TomH_606","link":" https://dl.dropboxusercontent.com/s/d8ff5pyt32vgmva/Tom%20H.wav?dl=1"},
    {"name":"TomH_Hum","link":"https://dl.dropboxusercontent.com/s/9jyau7m54bb1x5t/Tom-07.wav?dl=1"},
    {"name":"TomH_Zap","link":"https://dl.dropboxusercontent.com/s/km4zvtix9ha8z24/Tom-09.wav?dl=1"},
]

TomM_list = [
    {"name":"TomM_808","link":"https://dl.dropboxusercontent.com/s/7h29hztooqitgnt/Tom%20M.wav?dl=1"},
    {"name":"TomM_909","link":"https://dl.dropboxusercontent.com/s/5nip69k7ky7hedi/Tom%20M.wav?dl=1"},
    {"name":"TomM_Yamaha","link":"https://dl.dropboxusercontent.com/s/5rzionupibedj7z/TOMS_003.wav?dl=1"},
    {"name":"TomM_Soft","link":"https://dl.dropboxusercontent.com/s/b3gcwrdan6d2u10/TOMS_036.wav?dl=1"},
    {"name":"TomM_Ring","link":"https://dl.dropboxusercontent.com/s/59ay4mp3em8a630/Tom-02.wav?dl=1"},
    {"name":"TomM_Akai","link":"https://dl.dropboxusercontent.com/s/b5sy4v0779c7zev/Tom%20M.wav?dl=1"},
    {"name":"TomM_Ninja","link":"https://dl.dropboxusercontent.com/s/evgrbfb186cxy2w/Tom%20M.wav?dl=1"},
    {"name":"TomM_Linn","link":"https://dl.dropboxusercontent.com/s/cmfwzmou3s9v9zu/Tom-03.wav?dl=1"},
    {"name":"TomM_Python","link":"https://dl.dropboxusercontent.com/s/2bsll53nbw6acai/Tom-01.wav?dl=1"},
    {"name":"TomM_Mid","link":"https://dl.dropboxusercontent.com/s/sq5fm7jqvdecfkp/MT0D7.WAV?dl=1"},
]

TomL_List = [
    {"name":"TomL_808","link":"https://dl.dropboxusercontent.com/s/4i2krdetdv3dify/Tom%20L.wav?dl=1"},
    {"name":"TomL_909","link":"https://dl.dropboxusercontent.com/s/grsxt9aczenmog5/Tom%20L.wav?dl=1"},
    {"name":"TomL_Linn","link":"https://www.dldropboxusercontent.com/s/k0txr1683qx2jg7/Tom%20L.wav?dl=1"},
    {"name":"TomL_Thud","link":"https://dl.dropboxusercontent.com/s/z4k1uag8gbh61pe/DT_Perc_thud.wav?dl=1"},
    {"name":"TomL_Dojo","link":"https://dl.dropboxusercontent.com/s/r45gg0mt3xorg72/Tom-01.wav?dl=1"},
    {"name":"TomL_Real","link":"https://dl.dropboxusercontent.com/s/1zwro9qd7wfiqu3/Real.wav?dl=1"},
    {"name":"TomL_505","link":"https://dl.dropboxusercontent.com/s/azitvjmxk41uzhi/Tom%20L.wav?dl=1Ride"},
    {"name":"TomL_Sakata","link":"https://dl.dropboxusercontent.com/s/wpgoslcqzx8v04t/Tom-04.wav?dl=1"},
    {"name":"TomL_Comp","link":"https://dl.dropboxusercontent.com/s/4keab0nafcn3ym4/Tom%20L.wav?dl=1"},
    {"name":"TomL_Epic","link":"https://dl.dropboxusercontent.com/s/nslpqnam6i2r6xh/Toml%20L-03.wav?dl=1"},
]

Crash_List = [
    {"name":"Crash_Real","link":"https://dl.dropboxusercontent.com/s/m0ebmc9r78zteks/Real.wav?dl=1"},
    {"name":"Crash_909","link":"https://dl.dropboxusercontent.com/s/x93vff8mtbwlvab/Crash.wav?dl=1"},
    {"name":"Crash_Django","link":"https://dl.dropboxusercontent.com/s/6kqrj2kxr87mnaj/Crash-03.wav?dl=1"},
    {"name":"Crash_Shimmer","link":"https://dl.dropboxusercontent.com/s/cn32h9xn6w1rtel/Shimmer.wav?dl=1"},
    {"name":"Crash_Rough","link":"https://dl.dropboxusercontent.com/s/nd0ecyc23ifcyrf/Rough.wav?dl=1"},
    {"name":"Crash_Python","link":"https://dl.dropboxusercontent.com/s/zba2djye2o2x5of/Crash-01.wav?dl=1"},
    {"name":"Crash_Dull","link":"https://dl.dropboxusercontent.com/s/v7j7mex0r003vf2/Crash.wav?dl=1"},
    {"name":"Crash_Bold","link":"https://dl.dropboxusercontent.com/s/pyom0bgpl8mught/Crash.wav?dl=1"},
    {"name":"Crash_808","link":"https://dl.dropboxusercontent.com/s/td2054lys8qiywh/Crash-01.wav?dl=1"},
    {"name":"Crash_Chill","link":"https://dl.dropboxusercontent.com/s/qr9db32zrbivunp/Crash-02.wav?dl=1"},
]

Ride_List = [
    {"name":"Ride_909","link":"https://dl.dropboxusercontent.com/s/s6tp9jy5v71z1up/Ride.wav?dl=1"},
    {"name":"Ride_Z","link":"https://dl.dropboxusercontent.com/s/xz37o5has4lbx3b/DT_RD_zildjan.WAV?dl=1"},
    {"name":"Ride_Python","link":"https://dl.dropboxusercontent.com/s/fyzfrjiov1qef76/Ride-01.wav?dl=1"},
    {"name":"Ride_Django","link":"https://dl.dropboxusercontent.com/s/2z1m8p2a5t64czb/Ride.wav?dl=1"},
    {"name":"Ride_Ninja","link":"https://dl.dropboxusercontent.com/s/u6ruquoumq42o2l/Ride-01.wav?dl=1"},
    {"name":"Ride_Dojo","link":"https://dl.dropboxusercontent.com/s/ca5937w72silm4t/Ride.wav?dl=1"},
    {"name":"Ride_Short","link":"https://dl.dropboxusercontent.com/s/s5uw4bfr7yr0asi/Ride.wav?dl=1"},
    {"name":"Ride_MPC","link":"https://dl.dropboxusercontent.com/s/in294blswhleios/Ride.wav?dl=1"},
    {"name":"Ride_Linn","link":"https://dl.dropboxusercontent.com/s/mmnxkmaazrfvu3n/Ride.wav?dl=1"},
    {"name":"Ride_Bright","link":"https://dl.dropboxusercontent.com/s/i45g4rp0pm5mkdz/RIDED8.WAV?dl=1"},
]

Perc_List = [
    {"name":"Perc_Bit","link":"https://dl.dropboxusercontent.com/s/pwmqqwkg2mpo6jt/STAY_SE_00014.wav?dl=1"},
    {"name":"Perc_Short","link":"https://dl.dropboxusercontent.com/s/b62wjma4uv6eixt/Percussion%206.wav?dl=1"},
    {"name":"Perc_Stick","link":"https://dl.dropboxusercontent.com/s/77lkz9sar6wzne5/Stick.wav?dl=1"},
    {"name":"Perc_Chime","link":"https://dl.dropboxusercontent.com/s/6twaympvyf1f387/Chime.wav?dl=1"},
    {"name":"Perc_Cowbell","link":"https://dl.dropboxusercontent.com/s/v8vgkpso76tyvgf/Cowbell.wav?dl=1"},
    {"name":"Perc_Flick","link":"https://dl.dropboxusercontent.com/s/xm3f3ki2m7me9gk/Flick01.wav?dl=1"},
    {"name":"Perc_808Bell","link":"https://dl.dropboxusercontent.com/s/0lax1zfip695jl6/Perc_808bell.wav?dl=1"},
    {"name":"Perc_Vox","link":"https://dl.dropboxusercontent.com/s/k5sfgnbmluycycs/Perc_vox.wav?dl=1"},
    {"name":"Perc_Clap","link":"https://dl.dropboxusercontent.com/s/l3z7xlm99yvveso/Clap.wav?dl=1"},
    {"name":"Perc_Tambourine","link":"https://dl.dropboxusercontent.com/s/1h2d7rf83jl6pgv/Tambourine.wav?dl=1"},
]

'''creator=User.objects.get(id=request.session['user_id'])
def generate(request):
    kit = Kit.objects.create(
        #creator=User.objects.get(id=request.session['user_id']),
        title=request.POST['title'],
        #kick=kick_list[] #ran-int 0-9
        """snare=request.POST['snare'],
        HHcl=request.POST['HHcl'],
        HHop=request.POST['HHop'],
        crash=request.POST['crash'],
        ride=request.POST['ride'],
        tom_h=request.POST['tom_h'],
        tom_m=request.POST['tom_m'],
        tom_l=request.POST['tom_l'],
        perc=request.POST['perc'],"""
    )
    kit.save()'''

print(random.choice(snare_list))


"""user = User.objects.get(id=request.session['user_id'])
    user_kits = Kit.objects.filter(creator=user.id)
    other_kits = Kit.objects.exclude(creator=user.id)
    context = {
        "user": user,
        "user_kits": user_kits,
        "other_kits": other_kits,"""
