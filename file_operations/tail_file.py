from sh import tail
# runs forever
mongo_file = r"D:\MongoDB\Server\4.2\log\mongod.log"
for line in tail("-f", mongo_file, _iter=True):
    print(line)