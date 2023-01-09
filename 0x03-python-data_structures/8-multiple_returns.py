#!/usr/bin/python3
def multiple_returns(sentece):
    s = sentece
    return tuple([len(s), s[0]]) if len(s) > 0 else tuple([0, None])
