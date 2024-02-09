### Clonando repositório
- git clone  link-do-repositorio
*Cria um repositório local a partir de um repositório remoto*

### Status
- git status  
*Informa o status do git*

### Commit
- git add . 
- git add -A  
*Adiciona todas as mudanças ao próximo commit.*
- git commit -m "Mensagem do commit": Realiza um commit com a mensagem fornecida. 

### Atualizar repositório remoto
- git push  
*Envia os commits do nosso repositório local ao repositório remoto*
- git remote add upstream link-do-github  


### Atualizar repositório local
|Comando                  | Função                                                                              |  
|----                     |                       -----------------------------                                 |
| git remote show origin  | *Verifica se nosso repositório local está atualizado com o repositório remoto*      |
| git pull                | *Atualiza nosso repositório local com as últimas informações no repositório remoto* *Importante observar que atualiza o local com o remoto da respectiva branch apenas* |