# Base de Conhecimento

## Fonte dos Dados
Os dados foram criados a partir das aulas de DevSecOps da DIO e da documentação oficial, organizados manualmente para este protótipo.

## Formato
O agente usará um arquivo JSON em `data/devsecops_conceitos.json` com pares de pergunta e resposta.

## Conteúdo da Base (15 itens iniciais)

1.  **O que é DevSecOps?** - Uma abordagem que incorpora segurança desde o início do desenvolvimento.
2.  **Quais as 5 fases?** - Planejamento, Desenvolvimento, Testes, Implantação, Operações.
3.  **Por que precisamos de DevSecOps?** - Para reduzir o tempo de correção de falhas de segurança e acelerar a entrega segura.
4.  **O que é Shift Left?** - Trazer a segurança para o início do ciclo de desenvolvimento.
5.  **O que é SAST?** - Análise de segurança no código-fonte (estática).
6.  **O que é DAST?** - Análise de segurança na aplicação rodando (dinâmica).
7.  **Ferramenta de Planejamento seguro?** - Threat Modeling.
8.  **Ferramenta de Desenvolvimento seguro?** - Linters de segurança, SonarQube.
9.  **O que é IaC?** - Infrastructure as Code, e deve ser verificado por segurança.
10. **O que é um pipeline seguro?** - Pipeline CI/CD com etapas de scan de vulnerabilidades.

## Regras do Agente
- Só responder com base nesses dados
- Se a pergunta não estiver aqui, responder: "Ainda não tenho essa informação na minha base sobre DevSecOps"
- Nunca inventar ferramenta ou conceito
