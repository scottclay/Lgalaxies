def fit_scatter(x, y, ret_n=False, ret_sterr=False, ret_median=False, nbins=10):
    '''
    Bins scattered points and fits with error bars
    '''
    import numpy as np
    import scipy.stats

    n, _ = np.histogram(x, bins=nbins)
    sy, _ = np.histogram(x, bins=nbins, weights=y)
    sy2, _ = np.histogram(x, bins=nbins, weights=y*y)
    mean = sy / n
    std = np.sqrt(sy2/n - mean*mean)

    bin_centres = (_[1:] + _[:-1])/2.

    if ret_sterr:
        stderr = std/np.sqrt(n)
        if ret_n:
            if ret_median:
                median = scipy.stats.binned_statistic(x, y, statistic='median', bins=nbins)[0]
                mederr = std*1.2533
                return bin_centres, mean, std, stderr, n, median, mederr
            return bin_centres, mean, std, stderr, n
        return bin_centres, mean, std, stderr

    if ret_n:
        if ret_median:
            median = scipy.stats.binned_statistic(x, y, statistic='median', bins=nbins)
            mederr = std*1.2533
            return bin_centres, mean, std, n, median, mederr
        return bin_centres, mean, std, n
    return bin_centres, mean, std    

def fit_median(x,y,nbins=10):
    import numpy as np
    import scipy.stats

    stats = scipy.stats.binned_statistic(x, y, statistic='median', bins=nbins)
    median = stats[0]
    bin_edges = stats[1]
    bin_centres = (bin_edges[1:] + bin_edges[:-1])/2.

    per_50=np.zeros(len(bin_centres))
    per_16=np.zeros(len(bin_centres))
    per_84=np.zeros(len(bin_centres))
    per_25=np.zeros(len(bin_centres))
    per_75=np.zeros(len(bin_centres))
    
    for i in range(0,len(bin_centres)):
        try:   
            idx = np.where( (x>bin_edges[i]) & (x<bin_edges[i+1]) )
            yy = y[idx]
            per_50[i] = (np.percentile(yy,50))
            per_16[i] = (np.percentile(yy,16))
            per_84[i] = (np.percentile(yy,84))
            per_25[i] = (np.percentile(yy,25))
            per_75[i] = (np.percentile(yy,75))
        except IndexError:
            pass
    per_50[per_50==0]=np.nan
    per_16[per_16==0]=np.nan
    per_84[per_84==0]=np.nan
    per_25[per_25==0]=np.nan
    per_75[per_75==0]=np.nan

    return median, bin_centres, per_50,per_16,per_84,per_25,per_75
        
        
        
        
        
        
        
        
        
        
        
    