<template>
    <div class="block p-2 space-y-4 w-4/5 ">
        <div :key="post.title" v-for="post in posts">
            <div class="bg-gray-50 border rounded border-gray-100 shadow-sm divide-y" >
                <div class="p-2" >
                    <span class="flex justify-between">
                        <h1 class="text-base md:text-2xl pr-4 font-semibold ">{{post.title}}</h1>
                        <svg @click="$emit('deletedPost',post.id)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                            class="w-6 h-6 pt-2 cursor-pointer">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                        </svg>
                    </span>
                    <p class="text-sm md:text-lg break-all">{{post.content}}</p>
                </div>
                <div class="flex justify-start text-xs lg:text-lg"> 
                    <span :class="{'myclass':post.status}" class="flex p-1 m-1 rounded-lg text-center cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                                class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M6.633 10.5c.806 0 1.533-.446 2.031-1.08a9.041 9.041 0 012.861-2.4c.723-.384 1.35-.956 1.653-1.715a4.498 4.498 0 00.322-1.672V3a.75.75 0 01.75-.75A2.25 2.25 0 0116.5 4.5c0 1.152-.26 2.243-.723 3.218-.266.558.107 1.282.725 1.282h3.126c1.026 0 1.945.694 2.054 1.715.045.422.068.85.068 1.285a11.95 11.95 0 01-2.649 7.521c-.388.482-.987.729-1.605.729H13.48c-.483 0-.964-.078-1.423-.23l-3.114-1.04a4.501 4.501 0 00-1.423-.23H5.904M14.25 9h2.25M5.904 18.75c.083.205.173.405.27.602.197.4-.078.898-.523.898h-.908c-.889 0-1.713-.518-1.972-1.368a12 12 0 01-.521-3.507c0-1.553.295-3.036.831-4.398C3.387 10.203 4.167 9.75 5 9.75h1.053c.472 0 .745.556.5.96a8.958 8.958 0 00-1.302 4.665c0 1.194.232 2.333.654 3.375z" />
                        </svg>
                        <button @click="$emit('liked',post.id)">Like</button>
                    </span>
                    <span class="flex p-1 m-1 rounded-lg text-center cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                            class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M2.25 12.76c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.076-4.076a1.526 1.526 0 011.037-.443 48.282 48.282 0 005.68-.494c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z" />
                        </svg>
                        <button @click="$emit('id',post.id)">Comment</button>
                    </span>
                </div>
            </div>
            <div v-if="(post.comment.length > 0)" >
                <span :key="comment" v-for="comment in post.comment">
                    <p class="text-xs lg:text-sm  px-2 bg-gray-200 rounded-full mt-0.5 mb-1">{{comment}}</p>
                </span>
            </div>
        </div>
        <div v-if="newPostSection">
            <form @submit.prevent="post">
                <div class="grid justify-items-stretch space-y-1">
                    <input class="p-1 m-2 border border-gray-200 rounded-lg" type="text" placeholder="Title" v-model="title">
                    <textarea class="p-1 m-2 border border-gray-200 rounded-lg" type="text" placeholder="Content" v-model="content" required></textarea>
                </div>
                <div class="flex justify-center">
                    <button class="btn bg-blue-500" type="submit">Post</button>
                    <button class="btn bg-red-500" @click="close">close</button>
                </div>
            </form>
        </div>
        <div v-if="newCommentSection">
            <form @submit.prevent="add">
                <div class="flex justify-center">
                    <textarea class="p-1 m-2 w-2/3 border border-gray-200 rounded-lg" type="text" placeholder="Write a comment..." v-model="comment"></textarea>
                    <button class="btn bg-blue-500" type="submit">Add</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PostsName',
    data() {
        return {
            title: '',
            content: '',
            comment: '',
      }  
    },
    props: {
        posts: Array,
        newPostSection: Boolean,
        newCommentSection: Boolean,
    },
    methods:{
        post(){
            const newPost = {
                // id: ((Math.random()) * 10000).toFixed(0),
                title: this.title,
                content: this.content,
                status: false,
                comment:''
            };
            this.title = '' 
            this.content = ''
            this.$emit('newPost',newPost)
        },
        close() {
            this.$emit('close')
        },
        add() {
            this.$emit('comment', this.comment)
            this.comment = ''
        }
    }
}
</script>


<style scoped>
    .myclass{
        background: rgb(4, 161, 252);
    }
</style>