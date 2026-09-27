# 🛡️ SecOps Assistant - Agente Inteligente de DevSecOps com IA Generativa

> Projeto adaptado do Lab DIO "Agente Financeiro" para a temática DevSecOps

### 🔗 Repositório
https://github.com/nikolaspeixoto188-png/dio-lab-bia-do-futuro

### Contexto
Os assistentes virtuais no setor financeiro evoluiram para agentes inteligentes e proativos. Adaptei o conceito para **Segurança em Desenvolvimento (DevSecOps)**, onde o problema é o mesmo: devs deixam segurança para o final e geram vulnerabilidades caras.

Neste desafio, prototipei um agente que utiliza IA Generativa para:
*   Antecipar dúvidas sobre segurança ao invés de só responder
*   Personalizar explicações com base no nível do iniciante
*   Cocriar soluções seguras de forma consultiva
*   Garantir segurança e confiabilidade nas respostas (anti-alucinação via base JSON)

### Como Funciona
1.  **Base de Conhecimento:** `data/devsecops_conceitos.json` com 10 perguntas curadas sobre as 5 fases
2.  **Prompt Principal:** `docs/03-prompts.md` - instrui o bot a nunca inventar
3.  **Aplicação:** `src/app.py` em Streamlit que faz RAG simples

### As 5 Fases do DevSecOps implementadas
1. Planejamento (Threat Modeling)
2. Desenvolvimento (SAST)
3. Testes (DAST, SCA)
4. Implantação (IaC Seguro)
5. Operações (Monitoramento)

### Como Rodar
```bash
pip install -r src/requirements.txt
streamlit run src/app.py
