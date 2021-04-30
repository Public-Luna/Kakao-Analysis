<template>
  <div id="home">
    <b-container class="section left">
      <div>
        <p class="title">KakaoTalk Analysis</p>
        <p class="subtitle">
          카카오톡 로그! 완벽하게 분석해드립니다! <br>
          업로드된 개인정보와 카카오톡 로그는 서버에 저장되지 않기 때문에 걱정하실 필요 없습니다! <br>
        </p>
        <router-link to="upload"><b-btn variant="outline-dark" size="lg">Get Started</b-btn></router-link>
      </div>
    </b-container>

    <b-container class="section right">
      <div>
        <p class="title">Contribute to this project</p>
        <p class="subtitle">
          누구나 프로젝트에 참여하여 기여할 수 있습니다. <br>
          <b-badge>웹개발</b-badge> <b-badge>시각화</b-badge> <b-badge>데이터분석</b-badge> <br>
        </p>
        <a href="mailto:luna20617@gmail.com"><b-btn variant="outline-dark" size="lg">Contact</b-btn></a>
      </div>
    </b-container>

    <b-container>
      <div style="height: 1000px;">
        어쩌구 저쩌구
      </div>
    </b-container>
  </div>
</template>

<style lang="scss" scoped>
  #home {
    width: 100%;
    .section {
      padding-top: 12%;

      &.left>* {
        text-align: left;
      }
      &.right>* {
        text-align: right;
      }
      p.title {
        font-size: 45px;
        margin-bottom: 0;
      }
      p.subtitle {
        font-size: 20px;
      }
    }
  }
</style>

<script>
  export default {
    components: {
      
    },
    data() {
      return {

      }
    },
    methods: {
      
    }
  }
</script>