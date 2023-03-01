import datetime
import locale

# Idioma "es-AR" (español de Argentina)
locale.setlocale(locale.LC_ALL, 'es-AR')

class Semana:
    # Clase que abstrae el comportamiento de una semana
    def GenerarSemana(self, fecha=datetime.datetime.now()):
        dias = {'Lunes': '',
                'Martes': '',
                'Miércoles': '',
                'Jueves': '',
                'Viernes': '',
                'Sábado': '',
                'Domingo': ''}

        dia = fecha
        t = datetime.timedelta(days=1)

        dias[dia.strftime('%A').title()] = dia.strftime('%d/%m')

        anterior = dia - t
        while  anterior.strftime('%A').title() != 'Domingo':
            dias[anterior.strftime('%A').title()] = anterior.strftime('%d/%m')
            anterior -= t

        siguiente = dia + t
        while siguiente.strftime('%A').title() != 'Lunes':
            dias[siguiente.strftime('%A').title()] = siguiente.strftime('%d/%m')
            siguiente += t

        print(dias)

y = datetime.date(2023,2,12)
x = Semana()
x.GenerarSemana(y)