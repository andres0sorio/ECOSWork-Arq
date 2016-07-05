from faker import Factory
import datetime
import time 
import random
import time
from JsonEpisodeHelper import JsonEpisodeHelper

drugs = ['dolex','advil','ultra','ibopruf','tylenol']
activities = ['work','sport','gym','tv','eating','reading']

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M:%S', prop)

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M:%S', prop)

def selectFromList(names):
    lucky_name = random.choice(names)
    return lucky_name
            
def create_fake_stuff(fake):
    """"""
    stuff = ["name","email" ]
    result = []
    for item in stuff:
	result.append( str(getattr(fake, item)()) )  
    ctime = datetime.datetime.now()
    ctimemili = time.mktime(ctime.timetuple())*1000 + ctime.microsecond/1000
    cedula = str(int(ctimemili))
    result.append( cedula[4:len(cedula)] )
    #print randomDate("1/1/2008 1:30:00", "1/1/2016 4:50:00", random.random())
    return result

def create_fake_episode():
    """"""
    episode_date = randomDate("1/1/2008 1:30:00", "1/1/2016 4:50:00", random.random()).split()
    date=episode_date[0]
    time=episode_date[1]
    nivel_dolor = random.randint(1,10)
    medicamento = selectFromList(drugs)
    actividad = selectFromList(activities)
    episode = []
    episode.append(date)
    episode.append(time)
    episode.append(nivel_dolor)
    episode.append(medicamento)
    episode.append(actividad)
    return episode

if __name__ == "__main__":

    outfile = open('simulated_records.dat','w')

    for i in range(100):
    	fake = Factory.create()
    	pacient_data = create_fake_stuff(fake)
        for j in range(10):
            episode_data = create_fake_episode()
            jepisode = JsonEpisodeHelper()
            jepisode.setCedula(pacient_data[2])
            jepisode.setFecha(episode_data[0])
            jepisode.setHora(episode_data[1])
            jepisode.setNivel(episode_data[2])
            jepisode.setMedicamento(episode_data[3])
            jepisode.setActividad(episode_data[4])
            #print pacient_data
            #print episode_data
            print jepisode.getData()
            outfile.write(jepisode.getData() + '\n')

    outfile.close()
