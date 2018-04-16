import connexion
import six

from swagger_server.models.binary import BINARY  # noqa: E501
from swagger_server.models.decimal import DECIMAL  # noqa: E501
from swagger_server import util

def to_decimal(num):
    res, digit = 0, 0
    for i in range(len(num)-1, -1, -1):
        if num[i] == '1':
            res += pow(2, digit)
        digit += 1
    return res

def to_binary(num):
    num = int(num)
    tokens = []
    # while num > 0:
    #     tokens.append('1' if num%2 else '0')
    #     num /= 2
    # ----------------------------------------------
    # if num >1:
    #    to_binary(num//2)
    # tokens.append(str(num%2))
    
    #return "".join(reversed(tokens))
    # ----------------------------------------------
    return bin(num)[2:]


def binary_to_decimal(num):  # noqa: E501
    """binary_to_decimal

    Convert binary number to decimal # noqa: E501

    :param num: 
    :type num: str

    :rtype: DECIMAL
    """
    return to_decimal(num)


def decimal_to_binary(num):  # noqa: E501
    """decimal_to_binary

    convert decimal number to binary # noqa: E501

    :param num: 
    :type num: str

    :rtype: BINARY
    """
    return to_binary(num)
