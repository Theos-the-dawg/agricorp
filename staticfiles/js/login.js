        function togglePassword() {
            const pwd = document.getElementById('password');
            pwd.type = pwd.type === 'password' ? 'text' : 'password';
            document.getElementById('togglePwd').textContent = pwd.type === 'password' ? 'Show' : 'Hide';
        }

        function validateForm(e){
            const user = document.getElementById('username');
            const pwd = document.getElementById('password');
            const err = document.getElementById('loginError');
            err.textContent = '';
            if(!user.value.trim() || !pwd.value.trim()){
                e.preventDefault();
                err.textContent = 'Please enter both username and password.';
                return false;
            }
            const btn = e.target.querySelector('button[type=submit]');
            btn.disabled = true;
            btn.textContent = 'Logging in...';
            return true;
        }
        document.addEventListener('DOMContentLoaded', ()=>{
            const form = document.getElementById('loginForm');
            if(form) form.addEventListener('submit', validateForm);
        });