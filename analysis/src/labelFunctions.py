"""
Module to contain any functions that we use to assign labels to our datapoints
Given a data point, ie a date/period , we should look at the return and
say whether it was an up day or a down day - there can be a range of
integers to indicate if the returns were very high or very low
"""

from analysis.src.setup import *

def labels3(rtn):
    """This function does something.

    :param name: The name to use
    :type name: None
    :param state: None
    :type state: None
    :returns: None
    :raises: None
    """
    #print(rtn)
    if rtn is None or np.isnan(rtn):
        return None
    elif abs(rtn)<0.005:
        return  0
    elif abs(rtn)<0.015:
        return np.sign(rtn)*1
    elif abs(rtn)<0.025:
        return np.sign(rtn)*2
    else:
        return np.sign(rtn)*3

def labelId(rtn):
    """This function does something.

	:param name: The name to use
	:type name: None
	:param state: None
	:type state: None
	:returns: None
	:raises: None
	"""
    return rtn