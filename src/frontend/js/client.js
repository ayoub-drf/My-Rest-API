// const form = document.getElementById('login');

// let endPoint = 'http://127.0.0.1:8000/api';

// const loginProcess = (e) => {
//     e.preventDefault();
//     let formData = new FormData(form);
//     let data = Object.fromEntries(formData);
//     let token = `${endPoint}/token/`;

//     let options = {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(data)
//     };

//     fetch(token, options)
//     .then(r => r.json())
//     .then(data => {
//         setTokens(data);
//         getProductList();
//         return data;
//     })
//     .catch(error => {
//         console.error('Error:', error);  // Handle any errors
//     });
// };

// function setTokens(params) {
//     localStorage.setItem('access', params.access);
//     localStorage.setItem('refresh', params.refresh);
// };

// function getProductList() {
//     let endPoint = 'http://127.0.0.1:8000/api/products/';
    
//     let options = {
//         method: 'GET',
//         headers: {
//             'Authorization': `Bearer ${localStorage.getItem('access')}`,
//             'Content-Type': 'application/json',
//         },
//     };
//     fetch(endPoint, options)
//     .then(r => {
//         if (r.status === 200) {
//             console.log('Valid Token')
//             return r.json()
//         } else {
//             console.log('Invalid Token')
//             refreshToken(localStorage.getItem('refresh'))
//         }
//     })
//     .then(data => {
//         writeIntoRoot(data)
//         return data
//     }).catch((err) => {
//         console.log(err)
//     })
// };


// function writeIntoRoot(data) {
//     document.getElementById('root').innerHTML = JSON.stringify(data, null, 2)
    
// }

// if (localStorage.getItem('refresh')) {

// }

// function refreshToken(token) {
//     x = {
//         'refresh': token
//     }
//     const options = {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(x)
//     };
//     let url = `http://127.0.0.1:8000/api/token/refresh/`;
//     fetch(url, options)
//     .then(r => {
//         if (r.status === 200) {
//             return r.json()
//         } else {
//             console.log('Refresh Token has been expired')
//         }
//     })
//     .then(data => {
//         setTokens
//         localStorage.setItem('access', data.access)
//     }).catch((err) => {
//         console.log(err)
//     })

// }

// if (localStorage.getItem('refresh') && localStorage.getItem('access')) {
//     getProductList()
// }

// // python -m http.server 8111
// if (form) {
//     form.addEventListener("submit", loginProcess)
// };


const form = document.getElementById('search');

if (form) {
    form.addEventListener("submit", handleSearch);
}

function handleSearch(e) {
    e.preventDefault();

    const options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    };

    const formData = new FormData(form)
    const data = Object.fromEntries(formData)
    const SearchParams = new URLSearchParams(data)
    console.log(SearchParams.get('q'))
}