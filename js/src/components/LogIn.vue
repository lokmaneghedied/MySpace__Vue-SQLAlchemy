<template>
    <form @submit.prevent="logIn">
        <div class="grid justify-items-stretch p-2">
            <input class="p-3 m-2 border-2 border-gray-200 rounded-lg " type="email" placeholder="E-mail" v-model="email" required>
            <input class="p-3 m-2 border-2 border-gray-200 rounded-lg " type="password" placeholder="password" v-model="password" required>
            <button class=" p-3 m-2 rounded-lg bg-blue-600 text-center text-white cursor-pointer font-bold" type="submit">Log In</button>
        </div>
    </form>
</template>


<script>
export default {
    name: 'LogIn',
    data() {
        return {
            email: '',
            password:''
        }
    },
    methods: {
        logIn() {
            const user = {
                email: this.email,
                password: this.password
            };
            this.email = '';
            this.password = '';
            this.$emit('user',user)
        }
    }
}
</script>