<template>
  <div>
    <div class="self">

      <li class="liSelf">
        <div></div>
        <div class="myName nick">{{ snipingList[0][1].charAt(0).toUpperCase()+snipingList[0][1].slice(1) }}</div>
        <div class="game">{{ snipingList[0][0] }} 게임</div>
      </li>
    </div>
    <transition-group name="list" tag="ul">
      <li
        v-for="(summoner, index) in snipingList.slice(1)"
        v-bind:key="summoner[2]"
        class="shadow"
      >
        <div>{{ index + 1 }}위</div>
        <div class="nick">
          {{ summoner[1] }}
        </div>
        <div class="game">{{ summoner[0] }} 게임</div>
      </li>
    </transition-group>
  </div>
</template>

<script>
import paka from "./paka.json";
export default {
  data() {
    return {
      snipingList: paka.data,
    };
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0px;
  margin-top: 0;
  text-align: left;
  display: flex;
  flex-direction: column;
  align-items: center;

}
li {
  display: flex;
  justify-content: space-between;
  align-items:center;
  min-height: 50px;
  height: 50px;
  line-height: 50px;
  margin: 0.5rem 0;
  padding: 0 0.9rem;
  background: white;
  border-radius: 5px;

  width: 30vw;
}

.checkBtn {
  line-height: 45px;
  color: #62acde;
  margin-right: 5px;
}

.checkBtnCompleted {
  color: #b3adad;
}

.textCompleted {
  text-decoration: line-through;
  color: #b3adad;
}

.removeBtn {
  margin-left: auto;
  color: #de4343;
}

/*리스트 아이템 트랜지션*/
.list-enter-active,
.list-leave-active {
  transition: all 1s ease;
}

.list-enter,
.list-leave-to {
  opacity: 0;
  transform: translateY(30px);
}
.shadow {
  box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.03);
}

.self{
  display:flex;
  justify-content: space-around;
}

.liSelf{
  height:70px;
  width: 20vw;

  background-color:#F6B559;
}

.myName{
  font-size:2rem;
}

li div{
  flex:1;
}
.nick{
  flex:1;
  display: flex;
  justify-content: center;
}

.game{
  display: flex;
  flex-direction: row-reverse;
}

@media screen and (max-width:1200px) {
  li{
    width:70vw;
  }
  .liSelf{
    width:50vw;
  }
}
</style>
