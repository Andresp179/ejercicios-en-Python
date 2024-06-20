try:
    archivo=open('prueba.txt','w', encoding='utf8')
    archivo.write('Agregamos información')
except Exception as e:
   print(e)
finally:
   archivo.close()