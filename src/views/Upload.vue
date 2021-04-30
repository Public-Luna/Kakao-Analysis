<template>
  <div id="home">
    <b-container class="section left">
      <div>
        <p class="title">Upload</p>
        <p class="subtitle">
          업로드된 카카오톡 로그 데이터는 웹페이지를 닫는 순간 서버에서 소멸됩니다.<br>
        </p>
        <div class="block">
          <strong>Kakao Talk Log Upload</strong>
          <p>.txt 혹은 .csv 확장자의 카카오톡 로그파일을 선택해주세요.</p>
          <b-form-file
            style="max-width: 500px;"
            accept=".txt, .csv"
            v-model="file"
            name="file"
            :state="Boolean(file)"
            placeholder="파일을 선택하거나 이곳에 드래그 해주세요!"
            drop-placeholder="이곳에 드래그 해주세요!"
          ></b-form-file>
        </div>
        <div class="block">
          <strong>Privacy Policy</strong>
          <p>개인정보의 수집 및 이용목적</p>
          <p>
            "Kakao-Analysis Project"는 이용자가 업로드한 카카오톡 로그 파일을 통한 분석 서비스를 제공합니다.<br>
            위 서비스는 사용자의 데이터를 보관하지 않으며, 웹페이지를 종료한 시점에서 사용자가 업로드한 모든 데이터를 삭제합니다.
          </p>
          <b-form-checkbox-group
            v-model="agree"
            name="agree"
            :options="options"
            :state="state"
            unchecked-value="N"
          >
            <b-form-invalid-feedback :state="state">동의를 하지 않으셨습니다.</b-form-invalid-feedback>
          </b-form-checkbox-group>
        </div>
        <transition name="fade">
          <div class="block start" v-if="load">
            <strong>Getting Start</strong>
            <p>버튼을 누르면 분석센터로 이동합니다!</p>
            <b-button v-on:click="onSubmit" variant="outline-dark" size="lg">Let's Start!!</b-button>
          </div>
        </transition>
      </div>
    </b-container>
    <b-container>
      <div style="height: 1000px;">
        
      </div>
    </b-container>
  </div>
</template>

<style lang="scss" scoped>
  #home {
    width: 100%;
    .section {
      padding-top: 5%; /* 줄임 */

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
      .block {
        padding: 25px 0px 25px 10px;
      }
    }
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
</style>

<script>
  // import { mapState } from "vuex";
  import { UPLOAD_FILE } from "@/store/actions.type";

  export default {
    components: {
      
    },
    data() {
      return {
        agree: [],
        options: [{text: '개인정보 수집 및 이용목적에 동의합니다.', value: 'Y'}],
        file: null
      }
    },
    computed: {
      state() {
        return this.agree[0] == 'Y'
      },
      load() {
        return this.agree[0] == 'Y' && this.file
      }
    },
    methods: {
      onSubmit() {
        this.$store
          .dispatch(UPLOAD_FILE, { file: this.file })
          .then(() => this.$router.push({ path: "analysis" }));
      },
    },
  }
</script>