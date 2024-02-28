document.getElementById('postForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const text = document.getElementById('postText').value;
    const image = document.getElementById('postImage').files[0];
    
    if (text.trim() !== '' || image) {
      // Criar elemento de postagem
      const post = document.createElement('div');
      post.classList.add('post');
      const postContent = `
        <div class="post-header">
          <img src="profile-pic.jpg" alt="Profile Picture">
          <div class="post-info">
            <h2>Nome do Usuário</h2>
            <p>@usuario</p>
          </div>
        </div>
        <div class="post-content">
          <p>${text}</p>
          ${image ? `<img src="${URL.createObjectURL(image)}" alt="Post Image">` : ''}
        </div>
      `;
      post.innerHTML = postContent;
      
      // Adicionar postagem à timeline
      document.getElementById('timeline').prepend(post);
      
      // Limpar formulário
      document.getElementById('postText').value = '';
      document.getElementById('postImage').value = '';
    }
  });
  