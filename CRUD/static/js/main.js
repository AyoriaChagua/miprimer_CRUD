const btnd = document.querySelectorAll('.btn-delete')
if (btnd) {
    const btna = Array.from(btnd);
    btna.forEach((btn)=>{
        btn.addEventListener('click', (e) => {
            if(!confirm('Are you sure you want to delete it?')){
                e.preventDefault();
            }
        });
    });
}