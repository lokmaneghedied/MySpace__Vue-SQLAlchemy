<template>
    <div class="font-serif bg-blue-100 min-h-screen">
        <header class="border border-gray-200 shadow-xl text-blue-600 bg-white flex justify-between">
            <span class="p-2 truncate font-bold w-1/4 text-xs lg:text-xl">{{$route.params.email}}</span>
            <span>
                <span v-if="!x">
                    <button class="btn bg-blue-500 text-xs" @click="show">New Post</button>
                </span>
                <button class="btn bg-black text-xs" @click="logout">Log Out</button>
            </span> 
        </header>
        <div class="flex justify-center">
            <Posts class="block" :posts="this.posts" @newPost="newPost" @close="close" @comment="addComment" @liked="like" @id="newComment" :y="this.y" :x="this.x" />
        </div>
    </div>
</template>


<script>
import router from '../router'
import Posts from '../components/Posts.vue'
export default {
    name: 'UserName',
    data() {
        return {
            posts: [],
            x: false,
            y: false,
            id: '',
        }
    },
    components: {
        Posts,
    },
    methods: {
        newPost(post) {
            this.posts.push(post)
            this.x=!this.x
        },
        show() {
            this.x = !this.x
        },
        close() {
            this.x = !this.x
        },
        newComment(id) {
            this.y = !this.y
            this.id = id
        },
        addComment(ncomment) {
            this.posts.map((post) => {
                if (post.id == this.id) {
                    post.comments.push(ncomment)
                }
            })
            this.y = !this.y
        },
        logout() {
            router.push({ path: '/' })
        },
        like(id) {
            this.posts.map((post) => {
                if (post.id == id) {
                    post.status = !post.status
                }
            })
        }
    }
}
</script>