using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;

//THIS MY CODE FOR BLOCK KEYBOARD INPUT FOR WITH THE APPOINTED TIME
namespace inuyasha
{
    public partial class Form1 : Form
    {
     
          
        
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string[] source = { "Denis", "inuyasha", "USSR", "PCT" };

            for (int x = 0; x < source.Length; x++)
            {
                textBox1.AutoCompleteCustomSource.Add(source[x]);
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Disable.BlockInput(new TimeSpan(0,0,100));
            
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }

    public partial class Disable
    {
        [System.Runtime.InteropServices.DllImport("user32.dll", EntryPoint = "BlockInput")]
        [return: System.Runtime.InteropServices.MarshalAs(System.Runtime.InteropServices.UnmanagedType.Bool)]
        public static extern bool BlockInput([System.Runtime.InteropServices.MarshalAs(System.Runtime.InteropServices.UnmanagedType.Bool)] bool fBlockIt);

       public static void BlockInput(TimeSpan spn)
        {
            try
            {
                Disable.BlockInput(true);
                Thread.Sleep(spn);
            }
            catch(Exception)
            {

            }
        }
    }
}
