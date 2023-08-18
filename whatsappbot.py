# Importar bibliotecas
from selenium import webdriver
import time
from selenium.webdriver.common.by import By  # Importe a classe By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navegar até o whatsapp wb
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# Definir contatos e grupo e mensagem a ser enviada
contatos = ['Eu', 'Julinda']
mensagem = 'Testando a automação'
# Buscar contatos/grupos
wait_timeout = 30
element_locator = (By.XPATH, '//div[contains(@class, "selectable-text copyable-text")]')


def buscar_contato(contato):
    campo_pesquisa = WebDriverWait(driver, wait_timeout).until(
    EC.presence_of_element_located(element_locator)
)    #campo_pesquisa = driver.find_element_by_xpath(
    #    '//div[contains(@class, "selectable-text copyable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.enter()
    campo_pesquisa.send_keys(Keys.ENTER)
for contato in contatos:
    buscar_contato(contato)
    #enviar_mensagem(mensagem)
# Campo de pesquisa: 'selectable-text copyable-text'
# Campo de mensagem privada: 'selectable-text copyable-text'
# Buscar contatos grupos
# Enviar mensagens para o contato/grupo