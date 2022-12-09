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
            <Posts class="block" :posts="this.posts" @newPost="newPost" @close="close" @comment="addComment" @liked="like" @id="newComment" @deletedPost="deletedPost" :newCommentSection="this.newCommentSection" :newPostSection="this.newPostSection" />
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
            nPost:{},
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
        async deletedPost(id) {
            await fetch(`http://127.0.0.1:5000/posts/delete/${id}`, {
                method: 'DELETE',
                headers: { 'Content-type': 'application/json' },
            })
            this.posts = await this.fetchPosts()
        },
        async like(id) {
            await fetch(`http://127.0.0.1:5000/posts/editlike/${id}`, {
                method: 'PUT',
                headers: { 'Content-type': 'application/json' },
            })
            this.posts = await this.fetchPosts()
        },
        async addComment(ncomment) {
            this.posts.map((post) => {
                if (post.id == this.id) {
                    this.nPost.id = post.id,
                        this.nPost.title = post.title,
                        this.nPost.content = post.content,
                        this.nPost.status = post.status,
                        this.nPost.comment = ncomment
                }
            });
            await fetch('http://127.0.0.1:5000/posts/editcomment/', {
                method: 'PUT',
                headers: { 'Content-type': 'application/json' },
                body: JSON.stringify(this.nPost)
            }),
                this.newCommentSection = !this.newCommentSection
                this.posts = await this.fetchPosts()
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
        logout() {
            router.push({ path: '/' })
        },
    },
    async created() {
        this.posts = await this.fetchPosts()
    }
}
</script>