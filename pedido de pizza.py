from ast import And
from weakref import finalize
import PySimpleGUI as sg


def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]


    ]
    return sg.Window('login', layout=layout,finalize=True)

def janela_pedido():
    sg.theme('reddit')
    layout = [
        [sg.Text('fazer pedido')],
        [sg.Checkbox('Pizza de peppertoni', key='pizza1'),sg.Checkbox('Pizza de frango com catupiry', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]

    ]
    return sg.Window('montar pedido',layout=layout,finalize=True)

janela1,janela2 = janela_login(), None

while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event =='Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()    
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('foram solicitados uma pizza de peperoni e uma de frango com catupiry')
        elif values['pizza1'] == True:
            sg.popup('foram solicitados uma pizza de peperoni')
        elif values['pizza2'] == True:
            sg.popup('foram solicitados uma pizza de frango com catupiry')        
