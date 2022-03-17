from mcstatus import MinecraftServer
import random
#172

while True:
 
  first = str(random.randint(1,250))
  second = str(random.randint(1,250))
  third = str(random.randint(1,250))

  try:
    server = MinecraftServer.lookup("172." + str(first) + "." + str(second) + "." + str(third) + ":25565")


    status = server.status()
    print(f"The server has {status.players.online} players and replied in {status.latency} ms")


    latency = server.ping()
    print(f"The server replied in {latency} ms")


    query = server.query()
    print(f"The server has the following players online: {', '.join(query.players.names)}")
  except:
    print("FAIL")
