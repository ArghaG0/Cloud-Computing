# Lab 9: Develop MapReduce Application Using Hadoop Cluster Setup

**Aim:** To set up a Hadoop cluster in a Linux environment and develop, execute, and verify a MapReduce application using the Hadoop Distributed File System (HDFS) and Hadoop MapReduce framework.

---

## Task 1: Hadoop Cluster Setup

### Step 1: Verify Java Installation
Check if OpenJDK 17 is installed and verify both the runtime and compiler:
```bash
java -version
javac -version
```
*(If not installed, run `sudo apt update && sudo apt install openjdk-17-jdk -y`).*

### Step 2: Install Hadoop
Extract the Hadoop 3.x archive, move it to `/usr/local/hadoop`, and set ownership to your user account so Hadoop daemons have write permissions:
```bash
tar -xzf hadoop-3.5.0.tar.gz
sudo mv hadoop-3.5.0 /usr/local/hadoop
sudo chown -R $USER:$USER /usr/local/hadoop
```
Verify the binary:
```bash
/usr/local/hadoop/bin/hadoop version
```

### Step 3: Configure Environment Variables
1. Open `~/.bashrc`:
   ```bash
   nano ~/.bashrc
   ```
2. Add the following lines to the bottom of the file:
   ```bash
   export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
   export HADOOP_HOME=/usr/local/hadoop
   export HADOOP_HDFS_HOME=$HADOOP_HOME
   export HADOOP_MAPRED_HOME=$HADOOP_HOME
   export HADOOP_YARN_HOME=$HADOOP_HOME
   export HADOOP_COMMON_HOME=$HADOOP_HOME
   export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
   ```
3. Save (`Ctrl+O`, `Enter`), exit (`Ctrl+X`), and reload the configuration:
   ```bash
   source ~/.bashrc
   ```
4. Verify `JAVA_HOME` is also set inside `$HADOOP_HOME/etc/hadoop/hadoop-env.sh`:
   ```bash
   echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh
   ```
5. Test globally:
   ```bash
   echo $HADOOP_HOME
   hadoop version
   ```

### Step 4: Create HDFS Storage Directories
Create local directories for NameNode metadata and DataNode storage blocks:
```bash
mkdir -p /usr/local/hadoop/data/namenode
mkdir -p /usr/local/hadoop/data/datanode
```

### Step 5: Configure `core-site.xml`
Open `$HADOOP_HOME/etc/hadoop/core-site.xml` and update the `<configuration>` block:
```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

### Step 6: Configure `hdfs-site.xml`
Open `$HADOOP_HOME/etc/hadoop/hdfs-site.xml` and update the `<configuration>` block:
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///usr/local/hadoop/data/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///usr/local/hadoop/data/datanode</value>
    </property>
</configuration>
```

### Step 7: Configure `mapred-site.xml`
Open `$HADOOP_HOME/etc/hadoop/mapred-site.xml` and update the `<configuration>` block:
```xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.application.classpath</name>
        <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    </property>
</configuration>
```

### Step 8: Configure `yarn-site.xml`
Open `$HADOOP_HOME/etc/hadoop/yarn-site.xml` and update the `<configuration>` block:
```xml
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_HOME,PATH,LANG,TZ,HADOOP_MAPRED_HOME</value>
    </property>
</configuration>
```

### Step 9: Configure Worker Node
Open `$HADOOP_HOME/etc/hadoop/workers` and verify it contains:
```text
localhost
```

### Step 10: Configure Passwordless SSH
Install OpenSSH, enable the service, and configure passwordless SSH login for `localhost`:
```bash
sudo apt update && sudo apt install -y openssh-server openssh-client
sudo systemctl enable --now ssh
ssh-keygen -t ed25519 -P "" -f ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```
Verify SSH connectivity (type `yes` if prompted, then `exit`):
```bash
ssh localhost
exit
```

---

## Task 2: HDFS Configuration and Basic Operations

### Step 1: Format the NameNode
> **Warning:** Run this command **only once** during initial setup. Re-formatting later will erase existing HDFS metadata.
```bash
hdfs namenode -format
```

### Step 2: Start Hadoop Services
Start HDFS and YARN daemons:
```bash
start-dfs.sh
start-yarn.sh
```

### Step 3: Verify Running Daemons
Run `jps` to confirm all 5 Hadoop daemons are active:
```bash
jps
```
Expected processes:
- `NameNode`
- `DataNode`
- `SecondaryNameNode`
- `ResourceManager`
- `NodeManager`

### Step 4: Create HDFS Directory
```bash
hdfs dfs -mkdir -p /user/student/cloud-lab9/input
hdfs dfs -ls /user/student/cloud-lab9
```

### Step 5: Create Local Sample Input File
```bash
mkdir -p ~/cloud-lab9
cd ~/cloud-lab9

cat > input.txt <<EOF
cloud computing provides scalable resources
cloud computing uses distributed systems
hadoop processes large datasets
hadoop provides distributed storage
mapreduce processes data in parallel
mapreduce is used for large scale data processing
EOF

cat input.txt
```

### Step 6: Upload Input Data to HDFS
```bash
hdfs dfs -put input.txt /user/student/cloud-lab9/input/
hdfs dfs -ls /user/student/cloud-lab9/input
hdfs dfs -cat /user/student/cloud-lab9/input/input.txt
```

---

## Task 3: Develop MapReduce Application

### Step 1: Create `WordCount.java`
Inside `~/cloud-lab9`, create `WordCount.java`:
```bash
nano WordCount.java
```
Add the following Java source code:
```java
import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

    public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {
        private static final IntWritable one = new IntWritable(1);
        private Text word = new Text();

        public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            StringTokenizer itr = new StringTokenizer(value.toString());
            while (itr.hasMoreTokens()) {
                word.set(itr.nextToken().toLowerCase());
                context.write(word, one);
            }
        }
    }

    public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        private IntWritable result = new IntWritable();

        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            int sum = 0;
            for (IntWritable val : values) {
                sum += val.get();
            }
            result.set(sum);
            context.write(key, result);
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "word count");
        job.setJarByClass(WordCount.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

### Step 2: Compile the Java Program
```bash
export HADOOP_CLASSPATH=$(hadoop classpath)
javac -classpath "$HADOOP_CLASSPATH" -d . WordCount.java
```

### Step 3: Package into a JAR File
```bash
jar -cvf wordcount.jar *.class
ls
```
Confirm `wordcount.jar` and the `.class` files (`WordCount.class`, `WordCount$TokenizerMapper.class`, `WordCount$IntSumReducer.class`) appear in the directory.

---

## Task 4: Execute MapReduce & Analyze Results

### Step 1: Clean Any Existing Output Directory
```bash
hdfs dfs -rm -r /user/student/cloud-lab9/output 2>/dev/null || true
```

### Step 2: Submit the MapReduce Job
```bash
hadoop jar wordcount.jar WordCount /user/student/cloud-lab9/input /user/student/cloud-lab9/output
```

### Step 3: View Output Directory and Results
List the generated output files (`_SUCCESS` and `part-r-00000`):
```bash
hdfs dfs -ls /user/student/cloud-lab9/output
```
Display the computed word frequencies:
```bash
hdfs dfs -cat /user/student/cloud-lab9/output/part-r-00000
```
*Manual Verification Check:* Verify at least 5 words against `input.txt` (e.g., `cloud 2`, `computing 2`, `hadoop 2`, `mapreduce 2`, `distributed 2`).

### Task 4A: Explore Hadoop Web Interfaces
Open these URLs in your VM web browser to capture screenshots for your lab observation:
- **HDFS NameNode UI:** `http://localhost:9870` (Check HDFS overview, DataNodes, and Utilities -> Browse the file system)
- **YARN ResourceManager UI:** `http://localhost:8088` (Check Cluster metrics, Nodes, and completed `word count` application)

### Task 4B: Examine HDFS File Blocks
Check the file size, block count, and block locations:
```bash
hdfs fsck /user/student/cloud-lab9/input/input.txt -files -blocks
```

### Task 4C: Additional HDFS File Operations
1. **List files:**
   ```bash
   hdfs dfs -ls /user/student/cloud-lab9/input
   ```
2. **Download file from HDFS to local system:**
   ```bash
   hdfs dfs -get /user/student/cloud-lab9/input/input.txt downloaded.txt
   cat downloaded.txt
   ```
3. **Delete test file from HDFS** *(run only after taking all required screenshots)*:
   ```bash
   hdfs dfs -rm /user/student/cloud-lab9/input/input.txt
   ```

### Task 4D: Stop Hadoop Services
Shut down YARN and HDFS cleanly once the experiment is finished:
```bash
stop-yarn.sh
stop-dfs.sh
jps
```
Verify that only `Jps` remains running.