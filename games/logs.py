import logging

'''
   A formatação abaixo permite personalizarmos
   a forma como o log será mostrado para nós.
'''
# DateTime:Level:Arquivo:Mensagem
log_format = '%(asctime)s - %(levelname)s - %(filename)s.%(funcName)s - %(message)s'

'''
   Aqui definimos as configurações do módulo.

   filename = 'nome do arquivo em que vamos salvar a mensagem do log.'
   filemode = 'É a forma em que o arquivo será gravado.'
   level = 'Level em que o log atuará'
   format = 'Formatação da mensagem do log'
'''
logging.basicConfig(filename='games.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)

'''
   O objeto getLogger() permite que retornemos
   varias instancias de logs.
'''
# Instancia do objeto getLogger()
logger = logging.getLogger('root')
