<template>
    <div class="container p-2 w-3/4 rounded-lg bg-white shadow-2xl divide-y-2 space-y-3 md:w-1/3 md:h-2/3">
        <div class="flex justify-between">
            <div>
                <h1 class="font-bold">Sign Up</h1>
                <p>It’s quick and easy.</p>
            </div>
            <div>
                <svg @click="goBack" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                    class="w-6 h-6 text-red-500 cursor-pointer">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </div>
        </div>
        <form @submit.prevent="create">
            <div class="grid justify-items-stretch p-2">
                <input class="p-3 m-2 border-2 border-gray-200 rounded-lg" type="text" placeholder='First Name' v-model="firstName" required>
                <input class="p-3 m-2 border-2 border-gray-200 rounded-lg" type="text" placeholder='Last Name' v-model="lastName" required>
                <input class="p-3 m-2 border-2 border-gray-200 rounded-lg" type="email" placeholder='E-mail' v-model="email" required>
                <input class="p-3 m-2 border-2 border-gray-200 rounded-lg" type="password" placeholder='password' v-model="password" required>
                <button class="p-3 m-2 rounded-lg bg-green-500 text-center text-white cursor-pointer font-bold" type="submit">Create</button>
            </div>
        </form>
    </div>
</template>


<script>
export default {
    name: 'CreateNew',
    data() {
        return {
            firstName: '',
            lastName: '',
            email: '',
            password: '',
        }
    },
    methods: {
        create() {
            const newUser = {
                firstName: this.firstName,
                lastName: this.lastName,
                email: this.email,
                password: this.password
            };
            this.$emit('newUser', newUser);
            this.fName='';
            this.lName = '';
            this.email = '';
            this.password = '';
        },
        goBack() {
            this.$emit('goBack')
        }
    }
}
</script>


<!-- <div>
    <label for="birthday">Birthday</label>
    <input type="date" id="birthday" name="birthday">
</div>
<div>
    <label for="gender">Gender</label>
    <input type="radio" id="Male" name="gender" >
    <label for="Male">Male</label>
    <input type="radio" id="Female" name="gender">
    <label for="Female">Female</label>
</div> -->