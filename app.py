import whois
import requests

def get_domain_info(domain):
    try:
        # Obter informações do domínio
        w = whois.whois(domain)
        info = {
            "domain": domain,
            "owner": w.name,
            "email": w.email,
            "creation_date": w.creation_date,
            "expiration_date": w.expiration_date,
            "registrar": w.registrar,
        }
        return info
    except Exception as e:
        print(f"Erro ao obter informações do domínio: {e}")
        return None

def get_http_status(domain):
    try:
        response = requests.get(f'http://{domain}')
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return None

def main():
    print("Bem-vindo ao Site Info Extractor")
    domain = input("Digite o domínio (ex: example.com): ")
    
    # Extrair informações do domínio
    domain_info = get_domain_info(domain)
    if domain_info:
        print("\nInformações do Domínio:")
        for key, value in domain_info.items():
            print(f"{key.capitalize()}: {value}")
    
    # Checar o status HTTP do site
    status = get_http_status(domain)
    if status is not None:
        print(f"\nStatus HTTP do site: {status}")

if __name__ == "__main__":
    main()
