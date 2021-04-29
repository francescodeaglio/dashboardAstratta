import functools
from functools import partial
import os
import streamlit as st
from streamlit.report_thread import get_report_ctx

def st_functional_columns_old(lista, sizes=None):
       """
        Versione vecchia, lasciata solo per non pentirmi di averla cancellata
       """
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


def st_functional_columns(diz, sizes=None):
    """
    Da la possibilità di creare colonne quando si vuole, usando la programmazione funzionale.

    :param lista: lista di partial contenenti funzioni streamlit (st.selectbox, st.write ecc)
    :param sizes: dimensioni delle colonne. Opzionale, se non presente vengono create tutte della stessa dimensione. Solleva un'eccezione se la lista di funzioni e le dimensioni non hanno lo stesso numeri di elementi
    """
    if sizes is None:
        cols = st.beta_columns(len(diz.keys()))
    elif len(sizes) != len(diz.keys()):
        raise ValueError("func and size must have the same length")
    else:
        cols = st.beta_columns(sizes)

    i = 0
    ret = {}

    for el in diz:
        if type(diz[el]) == functools.partial:
            with cols[i]:
                ret[el] = diz[el]()
        else:
            ret[el] = None
        i+=1

    return ret



def get_session_id():
    import streamlit.report_thread as ReportThread
    from streamlit.server.server import Server
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)
    if session_info is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")
    return session_info.session.id