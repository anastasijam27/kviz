<script>
    import {PUBLIC_API_URL} from "$env/static/public";
    let email = '';
    let password = '';
    let error = '';
    async function handleSubmit(){
        const response = await fetch(`${PUBLIC_API_URL}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({email, password})
        });
        const data = await response.json();
        if (response.ok){
            window.location.href = '/dashboard';
        }
        else{
            error = data.error || 'Pogrešno uneti podaci. Pokušajte opet';
        }
    }
</script>

<div class="container">
    <h2 class="h2">Login</h2>
    <form on:submit|preventDefault={handleSubmit}>
        <div class="form-control">
            <input type="email" id=email bind:value={email} placeholder="Email">
        </div>
        <div class="form-control">
            <input type="password" id="password" bind:value={password} placeholder="Password">
        </div>
        <button type="submit" class="btn variant-filled">Login</button>
    </form>
</div>

<style>
    .container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
    }

    .form-control {
        margin-bottom: 20px;
    }

    input[type="email"],
    input[type="password"] {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 5px;
        color: black;
    }
    h2{
        padding: 10px;
    }
</style>