export default {
  computed: {
    filteredBlogs: function () {
      return this.product.filter((product) => {
        return product.title.match(this.search);
      });
    },
  },
};
