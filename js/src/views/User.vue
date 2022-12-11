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
            <Posts class="block" :posts="this.posts" :comments="this.comments" @newPost="newPost" @close="close" @addComment="addComment" @liked="like" @id="newComment" @deletedPost="deletedPost" @deletedComment ='deletedComment' :newCommentSection="this.newCommentSection" :newPostSection="this.newPostSection"   :changePostSection="this.changePostSection" @changePost="changePost" @changedPost="changedPost" />
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
            comments:[],
            newPostSection: false,
            newCommentSection: false,
            changePostSection :false,
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
            return data['posts']
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
        async changedPost(changedPost) {
            const nPost = {
                id: this.id,
                title: changedPost.title,
                content: changedPost.content
            }
            await fetch('http://127.0.0.1:5000/posts/editPost', {
                method: 'PUT',
                headers: { 'Content-type': 'application/json' },
                body: JSON.stringify(nPost)
            })
            this.posts = await this.fetchPosts()
        },
        async fetchComments() {
            const res = await fetch('http://127.0.0.1:5000/comments') 
            const data = await res.json()
            return data['comments']
        },
        async addComment(myComment) {
            const nComment = {
                post_id: this.id,
                content: myComment
            }
            if (myComment.length != 0) {
                await fetch('http://127.0.0.1:5000/comments/newcomment', {
                    method: 'POST',
                    headers: { 'Content-type': 'application/json' },
                    body: JSON.stringify(nComment)
                })
            }
            this.comments = await this.fetchComments()
            this.newCommentSection = !this.newCommentSection
        },
        async deletedComment(id) {
            await fetch(`http://127.0.0.1:5000/comments/delete/${id}`, {
                method: 'DELETE',
                headers: { 'Content-type': 'application/json' },
            })
            this.comments = await this.fetchComments()

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
        changePost(id) {
            this.changePostSection = !this.changePostSection
            this.id = id
        },
        logout() {
            router.push({ path: '/' })
        },
    },
    async created() {
        this.posts = await this.fetchPosts()
        this.comments = await this.fetchComments()
    }
}
</script>