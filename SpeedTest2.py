import speedtest
import datetime
import time
import requests




def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"] 
    

def main():
       
    with open ('SpeedTestResults.csv' , 'w', newline='\r\n') as f:
        f.write('Download,Upload,Ping,Datetime\n')
        for i in range(3):            #72 times a day 
            t = datetime.datetime.now()
            print('Making test #{}'.format(i+1))
            d, u, p = test()
            f.write('{:.2f} ,{:.2f},{},{}\n'.format(d / 1024, u / 1024, p , t))

            time.sleep(20)           #Every 20 minutes
       

            

if __name__ == '__main__':
    main()
            