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