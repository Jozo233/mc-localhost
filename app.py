import os 


heslo = "mc-localhost"
user = "mc-localhost"


print("Přihlašte se prosím")

answer = input("Jméno: ") 

if answer == user:
    answer = input("Heslo: ") 

    if answer == heslo:

        print("Přihlášen")
        
        print("---------------------------")
        print("|                         |") 
        print("|       mc-localhost      |")
        print("|                         |")
        print("---------------------------")

        print("[1] Vygenerovat server.properities")
        print("[2] Spustit server")
        print("[3] Odhlásit se")

        answer = input("Zvol, co mám udělat: ")

        if answer == "1": 

            print("Jaký mám používat port?")
            port = input() 

            print("Pro kolik hráčů má být server?")
            sloty = input() 

            print("Warez hráči true/false?")
            onlinemod = input() 

            with open("server.properties", "w") as file:
                file.write(f"""enable-jmx-monitoring=false 
rcon.port=41671 
level-seed= 
enable-command-block=true 
gamemode=survival 
enable-query=true 
generator-settings= 
level-name=world 
motd= 
query.port={port}
pvp=true 
generate-structures=true 
difficulty=easy 
network-compression-threshold=256 
max-tick-time=60000 
max-players={sloty}
use-native-transport=true 
enable-status=true 
online-mode={onlinemod}
allow-flight=true 
broadcast-rcon-to-ops=true 
view-distance=5 
max-build-height=256 
server-ip= 
allow-nether=true 
server-port={port}
sync-chunk-writes=true 
enable-rcon=false 
op-permission-level=4 
prevent-proxy-connections=false 
resource-pack= 
entity-broadcast-range-percentage=100 
player-idle-timeout=0 
rcon.password= 
force-gamemode=false 
debug=false 
rate-limit=0 
hardcore=false 
white-list=false 
broadcast-console-to-ops=true 
spawn-npcs=true 
spawn-animals=true 
snooper-enabled=true 
function-permission-level=2 
level-type=default 
text-filtering-config= 
spawn-monsters=true 
enforce-whitelist=false 
spawn-protection=0 
resource-pack-sha1= 
max-world-size=29999984 
# make by MC-LOCALHSOT""")

            print("server.properities byl úspěšně vygenerován")


        if answer == "2": 

            print("[1] Zapnout server.  RAM: 1024MB")
            print("[2] Zapnout server.  RAM: 2048MB")
            print("[3] Zapnout server.  RAM: 3072MB")
            print("[4] Zapnout server.  RAM: 4096MB")
            print("[5] Zapnout server.  RAM: 5120MB")
            print("[6] Zapnout server.  RAM: 6144MB")
            print("[7] Zapnout server.  RAM: 7168MB")
            print("[8] Zapnout server.  RAM: 8192MB")
            print("[9] Exit")

            answer = input("Zvol to co mám dělat: ")

            if answer == "1": 
                print("Spouštím server")
                os.system('java -Xms128M -Xmx1024M -jar server.jar nogui')

            if answer == "2": 
                print("Spouštím server")
                os.system('java -Xms128M -Xmx2048M -jar server.jar nogui')

            if answer == "3": 
                print("Spouštím server")
                os.system('java -Xms128M -Xmx3072M -jar server.jar nogui') 

            if answer == "4": 
                print("Spouštím server")
                os.system('java -Xms128M -Xmx4096M -jar server.jar nogui')
                
            if answer == "5": 
                print("Spouštím server")
                os.system('java -Xms128M -Xmx5120M -jar server.jar nogui') 

            if answer == "6": 
                print("Spouštím server")
                os.system('java -Xms128M -Xmx6144M -jar server.jar nogui') 
                
            if answer == "7":
                print("Spouštím server")
                os.system('java -Xms128M -Xmx7168M -jar server.jar nogui') 

            if answer == "8": 
                print("Spouštím server")
                os.system('java -Xms128M -Xmx8192M -jar server.jar nogui') 

            else: 
               print("Bye")

        else: 
            print("Bye")

    else: 
        print("Špatné heslo")
    
else: 
    print("Účet nebyl nalezen")
