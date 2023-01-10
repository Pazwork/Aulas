import pandas as pd
import matplotlib
import pyautogui

dados_2022 = pd.read_csv('dados2022.csv', encoding='utf-8', sep=';')

tipo_crime = dados_2022.groupby(['Tipo Crime'])
ocorrencia = tipo_crime.agg({'Ocorrências':sum})
print(ocorrencia)

plotPie = ocorrencia.plot.pie(subplots=True, figsize=(15,15),title = "Grafico do Crime")
plotPie[0].get_figure().savefig('dados4.png')


pyautogui.moveTo(38,663,2)
pyautogui.click(38,663)
pyautogui.write(' www.gmail.com', interval = 1.00)
pyautogui.hotkey('enter')
pyautogui.sleep(5)
pyautogui.moveTo(148,197)
pyautogui.click(148,197)
pyautogui.sleep(2)
pyautogui.write(' sandro.mesquita@professor.uniateneu.edu.br', interval = 1.00)
pyautogui.sleep(2)
pyautogui.click(971,423)
pyautogui.write('Trabalhos de Python')
pyautogui.sleep(2)
pyautogui.click(950,464)
pyautogui.write('Trabalhos em anexos.')
pyautogui.sleep(2)
pyautogui.click(1103,868)
pyautogui.sleep(2)
pyautogui.hotkey('enter')
pyautogui.sleep(2)
pyautogui.hotkey('enter')
pyautogui.sleep(2)
pyautogui.hotkey('enter')
pyautogui.sleep(2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('enter')
pyautogui.sleep(2)
pyautogui.hotkey('crtl','enter')

