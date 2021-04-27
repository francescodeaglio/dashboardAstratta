import functools
from functools import partial
import os
import streamlit as st

def st_functional_columns_old(lista, sizes=None):
       if sizes is None:
              cols = st.beta_columns(len(lista))
       elif len(sizes) != len(lista):

              raise ValueError("func and size must have the same length")
       else:
              cols = st.beta_columns(sizes)

       i = 0
       ret = []
       for el in lista:

              if len(el) == 0:
                  ret.append(None)
              else:
                  if el[0] == "write":
                         f = partial(cols[i].write, *el[1:])
                  elif el[0] == "beta_expander":
                         f = partial(cols[i].beta_expander, *el[1:])
                  elif el[0] == "selectbox":
                         f = partial(cols[i].selectbox, *el[1:])
                  elif el[0] == "slider":
                         f = partial(cols[i].slider, *el[1:])
                  elif el[0] == "multiselect":
                      f = partial(cols[i].multiselect, *el[1:])
                  elif el[0] == "date_input":
                      f = partial(cols[i].date_input, *el[1:])

                  ret.append(f())
              i += 1

       return ret


def st_functional_columns(lista, sizes=None):
    if sizes is None:
        cols = st.beta_columns(len(lista))
    elif len(sizes) != len(lista):
        raise ValueError("func and size must have the same length")
    else:
        cols = st.beta_columns(sizes)

    i = 0
    ret = []

    for el in lista:
        if type(el) == functools.partial:
            with cols[i]:
                ret.append(el())
        else:
            ret.append(None)
        i+=1

    return ret