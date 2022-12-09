<template>
    <div class="font-serif bg-blue-100 min-h-screen">
        <header class="border border-gray-200 shadow-xl text-blue-600 bg-white flex justify-between">
            <span class="p-2 truncate font-bold w-1/4 text-xs lg:text-xl">{{$route.params.email}}</span>
            <span>
                <span v-if="!newPostSection">
                    <button class="btn bg-blue-500 text-xs" @click="show">New Post</button>
                </span>
                <button class="btn bg-black text-xs" @click="logout">Log Out</button>
            </span> 
        </header>
        <div class="flex justify-center">
            <Posts class="block" :posts="this.posts" @newPost="newPost" @close="close" @comment="addComment" @liked="like" @id="newComment" :newCommentSection="this.newCommentSection" :newPostSection="this.newPostSection" />
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
            newPostSection: false,
            newCommentSection: false,
            id: '',
        }
    },
    components: {
        Posts,
    },
    methods: {
        async newPost(post) {
            await fetch('http://127.0.0.1:5000/posts/newPost', {
                method: 'POST',
                headers: { 'Content-type': 'application/json' },
                body: JSON.stringify(post)
            })
            this.posts = await this.fetchPosts()
            this.newPostSection = !this.newPostSection
        },
        async fetchPosts() {
            const res = await fetch('http://127.0.0.1:5000/posts')
            const data = await res.json()
            const myPosts = data['posts']
            myPosts.map((post) => {
                post['comment'] = post['comment'].split('/')
            })
            return myPosts
        },
        show() {
            this.newPostSection = !this.newPostSection
        },
        close() {
            this.newPostSection = !this.newPostSection
        },
        newComment(id) {
            this.newCommentSection = !this.newCommentSection
            this.id = id
        },
        addComment(ncomment) {
            this.posts.map((post) => {
                if (post.id == this.id) {
                    post.comment.push(ncomment)
                }
            })
            this.newCommentSection = !this.newCommentSection
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
    },
    async created() {
        this.posts = await this.fetchPosts()
    }
}
</script>