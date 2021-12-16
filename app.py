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

        print("[1] Vygenerovat server properities")
        print("[2] Spustit server")
        print("[3] Odhlásit se")

        answer = input("Zvol to co mám dělat: ")

        if answer == "1": 

            print("Jaký mám používat port?")
            port = input() 

            print("Pro kolik hráčů má být server?")
            sloty = input() 

            print("Varez hráči treu/false?")
            onlinemod = input() 

            file = open('server.properties', 'w')

            file.write('enable-jmx-monitoring=false \n')
            file.write('rcon.port=41671 \n')
            file.write('level-seed= \n')
            file.write('enable-command-block=true \n')
            file.write('gamemode=survival \n')
            file.write('enable-query=true \n')
            file.write('generator-settings= \n')
            file.write('level-name=world \n')
            file.write('motd= \n')
            file.write('query.port=' + port) 
            file.write(' \n')
            file.write('pvp=true \n')
            file.write('generate-structures=true \n')
            file.write('difficulty=easy \n')
            file.write('network-compression-threshold=256 \n')
            file.write('max-tick-time=60000 \n')
            file.write('max-players=' + sloty) 
            file.write('\n')
            file.write('use-native-transport=true \n')
            file.write('enable-status=true \n')
            file.write('online-mode=' + onlinemod) 
            file.write('\n')
            file.write('allow-flight=true \n')
            file.write('broadcast-rcon-to-ops=true \n')
            file.write('view-distance=5 \n')
            file.write('max-build-height=256 \n')
            file.write('server-ip= \n')
            file.write('allow-nether=true \n')
            file.write('server-port=' + port) 
            file.write('\n')
            file.write('sync-chunk-writes=true \n')
            file.write('enable-rcon=false \n')
            file.write('op-permission-level=4 \n')
            file.write('prevent-proxy-connections=false \n')
            file.write('resource-pack= \n')
            file.write('entity-broadcast-range-percentage=100 \n')
            file.write('player-idle-timeout=0 \n')
            file.write('rcon.password= \n')
            file.write('force-gamemode=false \n')
            file.write('debug=false \n')
            file.write('rate-limit=0 \n')
            file.write('hardcore=false \n')
            file.write('white-list=false \n')
            file.write('broadcast-console-to-ops=true \n')
            file.write('spawn-npcs=true \n')
            file.write('spawn-animals=true \n')
            file.write('snooper-enabled=true \n')
            file.write('function-permission-level=2 \n')
            file.write('level-type=default \n')
            file.write('text-filtering-config= \n')
            file.write('spawn-monsters=true \n')
            file.write('enforce-whitelist=false \n')
            file.write('spawn-protection=0 \n')
            file.write('resource-pack-sha1= \n')
            file.write('max-world-size=29999984 \n')
            file.write('# make by MC-LOCALHSOT')

            file.close() 

            print("Server  properities byl úspěšně vygenerován")


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
    print("Účet není nalezen")
