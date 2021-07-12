## 启动spark

./bin/spark-shell --master local[2]

## WebUi

http://127.0.0.1:4040/jobs/

## RDD

创建rdd
val rdd_one = sc.parallelize(Seq(1,2,3))
从文件创建rdd
val rdd_two = sc.textFile("README.md")
对rdd进行转换
val rdd_one_x2 = rdd_one.map(i => i * 2)

## action算子与tansformation算子

### transformation算子

map函数
val rdd_three = rdd_two.map(line => line.length)

flatMap函数
val rdd_three = rdd_two.flatMap(line => line.split(" "))
Array[String] = Array(#, Apache, Spark, "", Spark, is, a, unified, analytics, engine)

filter函数
val rdd_three = rdd_two.filter(line => line.contains("Spark"))

coalesce函数 合并分区
scala> val rdd_three = rdd_two.coalesce(1)
rdd_three: org.apache.spark.rdd.RDD[String] = CoalescedRDD[8] at coalesce at <console>:25
scala> rdd_three.partitions.length
res16: Int = 1

repartition函数 重新分区
scala> val rdd_three = rdd_two.repartition(5)
rdd_three: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[12] at repartition at <console>:25
scala> rdd_three.partitions.length
res18: Int = 5
 

