import speedtest
import datetime
import sched, time
import csv

a = sched.scheduler(time.time, time.sleep)


def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def main(sc):
    print ("Making Test 1")

    t = datetime.datetime.now()
    with open ('SpeedTestResults.csv' , 'w', newline='\r\n') as f:
        f.write('Download,Upload,Ping,Date time\n')
        for i in range(1):
            print('Making test #{}'.format(i+1))
            d, u, p = test()
            f.write('{:.2f} Kb/s,{:.2f} Kb/s,{},{}\n'.format(d / 1024, u / 1024, p , t))   

    a.enter(60,1,main, (sc,))

a.enter(60,1,main,(a,))
a.run()



if __name__ == '__main__':

    main()
                        