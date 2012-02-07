'''
Created on 2012-02-07

@author: aparkin
'''
from timeit import Timer

def timeruns(runs, num_iterations = 100):
    '''
    Time a series of code snippets, running each num_iterations times.  The 
    snippets are passed via the runs parameter, which is a list of tuples,
    each tuple containing

    1) the snippet to time
    2) a "setup" chunk of code (as per the Timer.timeit documentation)
    3) a human-readable label to associate with each run
    
    @type runs: [ (str, str, str) ]
    
    @return: a list of tuples, each tuple containing the human-readable label
    along with the time taken to run that snippet
    @rtype: [ ( str, float ) ]
    '''
    return [(label, Timer(cmd, imports).timeit(num_iterations))
      for cmd, imports, label in runs]

def format_runs(runresults):
    '''
    Format the results of a call to timeruns into a nice, easy-to-read string.
    
    @param runresults: the results of a call to timeruns()
    @type runresults: [ ( str, float ) ] 
    '''
    result = "Timing Results:\n%s\n" % ("-" * 20)
    minlabel, mintime = "Arbitrary label", 12319283719827319.0
    maxlabel, maxtime = "Arbitrary label", -1.0
    for label, time in runresults:
        result += "%s : %s\n" % (label, time)
        if time < mintime:
            mintime = time
            minlabel = label
        if time > maxtime:
            maxtime = time
            maxlabel = label
            
    result += "%s\n" % ("-" * 20)
    per_faster = round((1.0 - mintime / maxtime) * 100)

    result += ("Fastest time: %s - %s (%s%% faster than slowest)\n" % 
               (minlabel, mintime, per_faster))
    result += "Slowest time: %s - %s\n" % (maxlabel, maxtime)
    return result
