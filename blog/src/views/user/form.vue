<template>
  <div>
    <div v-for="(item, i) in divlist" :key="i" class="test">
      <h3>{{ item.name }}</h3>
      <div v-for="(item1, j) in item.children" :key="j">
        <h4>{{ item1.name }}</h4>
        <span v-for="(item2, k) in item1.children" :key="k" :class="j"
          >{{ item.id }}-{{ item1.id }}-{{ item2.id
          }}<input
            name="jack"
            type="text"
            :id="item.id + '-' + item1.id + '-' + item2.id"
        /></span>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      id: "",
      divlist: [
        {
          name: "大类1",
          id: 1,
          children: [
            {
              name: "小类1",
              id: 4,
              children: [
                {
                  name: "参数1",
                  id: 9
                }
              ]
            },
            {
              name: "小类2",
              id: 16,
              children: [
                {
                  name: "参数1",
                  id: 10
                },
                {
                  name: "参数2",
                  id: 11
                }
              ]
            }
          ]
        },
        {
          name: "大类2",
          id: 2,
          children: [
            {
              name: "小类1",
              id: 5,
              children: [
                {
                  name: "参数1",
                  id: 12
                }
              ]
            },
            {
              name: "小类2",
              id: 6,
              children: [
                {
                  name: "参数1",
                  id: 13
                }
              ]
            },
            {
              name: "小类3",
              id: 7,
              children: [
                {
                  name: "参数1",
                  id: 14
                }
              ]
            }
          ]
        },
        {
          name: "大类3",
          id: 3,
          children: [
            {
              name: "小类1",
              id: 8,
              children: [
                {
                  name: "参数1",
                  id: 15
                }
              ]
            }
          ]
        }
      ]
    };
  },
  methods: {
    getval() {
      var dom = document.getElementsByName("jack");
      let Ary = [];
      dom.forEach((item, i) => {
        let id = item.id;
        var idlist = id.split("-");
        let obj1 = {};
        let obj2 = {};
        let obj3 = {};

        obj1.id = idlist[0];

        obj2.parentId = idlist[0];
        obj2.id = idlist[1];

        obj3.parentId = idlist[1];
        obj3.id = idlist[2];
        obj3.name = item.value;

        Ary.push(obj1);
        Ary.push(obj2);
        Ary.push(obj3);
      });
      let newAry = [];
      let idlist = [];
      Ary.forEach(item => {
        let id = item.id;
        if (idlist.indexOf(id) == -1) {
          idlist.push(id);
          newAry.push(item);
        }
      });
      let result = this.toTree(newAry);
    },
    toTree(data) {
      let parents = data.filter(
        value => value.parentId == "undefined" || value.parentId == null
      );
      let children = data.filter(
        value => value.parentId !== "undefined" && value.parentId != null
      );
      let translator = (parents, children) => {
        parents.forEach(parent => {
          children.forEach((current, index) => {
            if (current.parentId === parent.id) {
              let temp = JSON.parse(JSON.stringify(children));
              temp.splice(index, 1);
              translator([current], temp);
              typeof parent.children !== "undefined"
                ? parent.children.push(current)
                : (parent.children = [current]);
            }
          });
        });
      };

      translator(parents, children);
      return parents;
    }
  }
};
</script>