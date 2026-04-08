import asyncio
from playwright.async_api import async_playwright

async def crawler_onde_assistir_spfc():
    async with async_playwright() as p:
        # Lançamos o browser
        browser = await p.chromium.launch(headless=False) 
        page = await browser.new_page()
        
        print("🔍 Passo 1: Buscando a notícia do próximo jogo...")
        await page.goto("https://ge.globo.com/futebol/times/sao-paulo/")

        # SELETOR TÉCNICO: Procuramos um link (a) que contenha 'onde-assistir' no endereço (href)
        # O '*' significa 'contém'
        selector_link = "a[href*='onde-assistir']"
        
        try:
            # Esperamos o link aparecer na home
            await page.wait_for_selector(selector_link, timeout=5000)
            
            # Pegamos o link real da notícia
            link_noticia = await page.get_attribute(selector_link, "href")
            print(f"🔗 Notícia encontrada: {link_noticia}")

            # Passo 2: Navegar para a notícia específica
            print("🚀 Navegando para os detalhes da transmissão...")
            await page.goto(link_noticia)

            # Passo 3: Extrair Horário e Canal
            print("📡 Extraindo informações de horário e transmissão...")

            transmissao_element = page.locator("li:has-text('Transmissão')")
            horario_element = page.locator("li:has-text('Horário')")
            
            # Verificamos se eles existem antes de extrair o texto
            info_transmissao = await transmissao_element.inner_text() if await transmissao_element.count() > 0 else "Não encontrado"
            info_horario = await horario_element.inner_text() if await horario_element.count() > 0 else "Não encontrado"

            print(f"\n⚽ INFORMAÇÕES DO JOGO")
            print(f"📺 {info_transmissao}")
            print(f"⏰ {info_horario}")

        except Exception as e:
            print(f"❌ Erro: Não foi possível encontrar a notícia de transmissão. {e}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(crawler_onde_assistir_spfc())